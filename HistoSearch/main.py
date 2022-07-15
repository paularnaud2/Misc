import os.path
import gl
import partools.utils as pt
from partools.tools import del_dup_list
from selenium.common.exceptions import TimeoutException

from partools.sel import g
import partools.sel.parse as p
from partools.sel import browse as b


def main():

    g.path = 'cache/'

    inp = 'files/url_in.txt'
    out = 'files/url_out.txt'
    ul = gen_ul(inp, out)
    out = []

    pt.log("Processing url list...")
    for url in ul:
        gl.nb_rec += 1
        gl.ha = pt.hash512(url)
        txt = load_txt(url)
        for s in txt:
            if pt.like_list(s, gl.SEARCH, False):
                out.append([url + ' ', s])
                gl.nb_res += 1

    out = del_dup_list(out)
    out_path = 'files/out.csv'
    pt.save_csv(out, out_path)
    s = f"Search over. {gl.nb_res} results found. The result was written to {out_path}"
    pt.log(s)


def gen_ul(inp, out):
    ul = pt.load_txt(inp)
    for i, url in enumerate(ul):
        if '#' in url:
            j = url.find('#')
            ul[i] = url[:j]
    ul = del_dup_list(ul)
    if gl.FILTER:
        ul = [e for e in ul if pt.like_list(e, gl.FILTER_URL, False)]
    else:
        ul = [e for e in ul if not pt.like_list(e, gl.FILTER_NOT_URL, False)]

    pt.save_list(ul, out)
    print(f"URL list saved to {out} ({len(ul)} records)")

    return ul


def load_src(url):
    if gl.SKIP_LOAD_SRC and not os.path.exists(f'{g.path}{gl.ha}.html'):
        try:
            pt.log(f"Processing url No. {gl.nb_rec}")
            b.load_webpage(url)
        except TimeoutException:
            pt.log(f"Warning: timeout for {url} ({g.path}{gl.ha}.txt)")
            pass
        b.save_source(gl.ha)
    b.load_source(gl.ha)
    return p.get_elt("/html/body")


def load_txt(url):

    path = f'{g.path}{gl.ha}.txt'
    if gl.SKIP_LOAD_SRC and not os.path.exists(path):
        src = load_src(url)
        if not src:
            pt.log(f"Warning: void text for {url}")
            return []
        out = []
        body = src[0]
        for e in body.itertext():
            s = e.strip('\n\t\xa0/ ')
            if len(s) > 50 and not pt.like_list(s, gl.FILTER_TXT):
                out.append(s)
        pt.save_list(out, path)
        pt.log(f"Text extracted and saved to {path}")

    out = pt.load_txt(path)

    return out


main()
