FILTER = False
SKIP_LOAD_SRC = True
SKIP_LOAD_TXT = True

nb_rec = 0
nb_res = 0
ha = ''

SEARCH = ["feu"]

FILTER_TXT = [
    '$(*',
    '(function*',
    '{',
    '}',
    '<',
    '>',
]

FILTER_URL = [
    "https://en.wikipedia.org",
    "https://fr.wikipedia.org",
]

FILTER_NOT_URL = [
    "https://en.wikipedia.org",
    "https://fr.wikipedia.org",
    "*.pdf",
    "*.png",
    "*.jpg",
    "*.svg",
    "impots.gouv",
    "chromedriver",
    "ubs.com",
    "bullionvault",
    "payment",
    "wordreference",
    "footprintnetwork",
    "hellobank",
    "jegeremacartenavigo",
    "xe.com",
    "ebanking",
    "amazon.com",
    "boursorama.com",
    "cairn.info",
    "https://m.facebook.com",
    "https://workspace*ubs.com*",
    "https://www.google.com/search",
    "https://mag.ubs.com/mobilepass",
    "https://fr.pornhub.com",
    "https://www.facebook.com",
    "https://ticktick.com",
    "https://www.youtube.com",
    "https://web.whatsapp.com",
    "https://www.amazon.fr",
    "https://www.wordreference.com",
    "https://mail.google.com",
    "http://www.synonymo.fr",
    "https://meta.swica.ch",
    "https://myswica.ch",
    "https://getadblock.com",
    "https://fr.wiktionary.org",
    "https://www.thetrainline.com",
    "https://www.thomann.de",
    "https://www.audible.fr",
    "https://book-gratuit.com",
    "https://www.google.com/maps",
    "https://translate.google.com",
    "https://misterbriquet.fr",
    "https://www.google.fr/maps",
    "https://www.larousse.fr",
    "https://ebanking-ch1.ubs.com",
    "https://boutique.groupepourlascience.fr",
    "https://accounts.google.com",
    "chrome-extension://",
    "file:///C:",
    "https://ch.oui.sncf",
    "https://chrome.google.com",
    "https://dict.leo.org",
    "https://docs.google.com",
    "https://donate.wikimedia.ch",
    "https://doodle.com",
    "https://drive.google.com",
    "https://fr.canon.ch",
    "https://get.adobe.com",
    "https://git-scm.com",
    "https://github.com",
    "Authentication",
    "https://joshwrightpiano",
    "https://messages.google.com",
    "https://music.youtube.com",
    "https://myaccount.google.com",
    "boutique",
    "https://onedrive.live.com",
    "https://paiement.systempay",
    "https://pay.google.com",
    "https://sh.ch",
    "https://sso.teachable.com",
    "https://stackoverflow.com",
    "https://support.google.com",
    "https://support.microsoft.com",
    "https://vscode-auth",
    "https://wifi.",
    "https://www.audible.de",
    "https://www.cdiscount.com",
    "https://www.linkedin.com",
    "https://www.lws.fr",
    "https://www.microsoft.com",
    "https://www.mythicsoft.com",
    "https://www.oui.sncf",
    "https://payment.datatrans",
    "coronavirus",
    "https://sh.impfung-covid",
    "http://localhost",
    "https://meisterkonzerte.ch/",
    "https://scienceetonnante.com",
    "https://wiki.kiwix.org",
    "thomann",
    "https://www.linternaute.fr/dictionnaire",
    "https://zamm.ch",
    "https://www.tgv-lyria.com",
    "https://www.swica.ch",
    "python",
    "https://www.kontakt-formular",
    "https://www.google.fr",
    "https://www.foobar2000.org",
    "https://www.ebay.com",
    "https://www.commentcamarche.net",
    "https://thepiratebay",
    "https://docs.microsoft.com",
    "http://0redirc.com",
    "http://archive.wikiwix.com/cache/index2.php?url=http%3A%2F%2Fdarwin.eeb.uconn.edu%2Fsimulations%2Fdrift.html",
    "vscode",
    "https://forums.commentcamarche.net/forum/affich-34205708-comment-ne-pas-recevoir-de-message-d-inconnus-sur-facebook",
    "https://scholar.google.ch/scholar_url?url=https://revistas.ucm.es/index.php/POSO/article/download/POSO0606130213A/22738/0&hl=fr&sa=X&ei=F6E9Yau1MoWImwHn6oWQAg&scisig=AAGBfm3mu2_vzRRIgQ7JnZj-Ecmf3L-L7w&oi=scholarr",
    "https://www.theatlantic.com/science/archive/2016/04/the-illusion-of-reality/479559/",
]
