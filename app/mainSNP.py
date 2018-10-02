from app import app
import requests
import threading
from bs4 import BeautifulSoup

from app.SNP import SNP

OBJs = []
ThreadOBJs = []

def filterURLs(input_urls):

    inputURLs = input_urls.split('\r\n')
    filteredURLs = []
    for url in inputURLs:
        filteredURLs.append(url)

    print(filteredURLs)
    create_workers(filteredURLs)
    return OBJs

def create_workers(filteredURLs):

    global OBJs
    OBJs = []
    global ThreadOBJs
    ThreadOBJs = []

    for url in filteredURLs:
        t = threading.Thread(target=work, args=(url,))
        t.daemon = True
        t.start()
        ThreadOBJs.append(t)

    for thread in ThreadOBJs:
        thread.join()


def work(url):

    responseObject = requests.get(url)
    sourceCode = responseObject.text
    soup = BeautifulSoup(sourceCode, 'lxml')
    # print(soup)

    snp = SNP(soup, sourceCode)
    browserTitle = snp.browser_title()
    breadcrumb =snp.breadcrumb()
    metaDescription =snp.meta_description()
    metaKeywords = snp.meta_keywords()
    pageTitle =snp.page_title()
    hero_image_list = snp.hero_image_link()
    hero_video = snp.hero_video()
    heroDescription = snp.hero_description()
    pricing = snp.pricing()
    tabs = snp.tabs()
    support =snp.support()
    features = snp.features()
    intelLogo = snp.intelLogo()
    technotes = snp.technote()

    print('\n\n\nbrowserTitle: '+browserTitle)
    print('\n\n\nbreadcrumb: '+str(breadcrumb))
    print('\n\n\nmetaDescription: '+metaDescription)
    print('\n\n\nmetaKeywords: '+metaKeywords)
    print('\n\n\npageTitle: '+pageTitle)
    print('\n\n\nhero_image_list: '+str(hero_image_list))
    print('\n\n\nhero_video: '+str(hero_video))
    print('\n\n\nheroDescription: '+str(heroDescription))
    print('\n\n\npricing: '+str(pricing))
    print('\n\n\ntabs: '+str(tabs))
    print('\n\n\nsupport: '+str(support))
    print('\n\n\nfeatures: '+str(features))
    print('\n\n\nIntel Logo: '+str(intelLogo))
    print('\n\n\nTechnotes: '+str(technotes))
