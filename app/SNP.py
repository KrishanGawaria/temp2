from app import app
from bs4 import BeautifulSoup
import requests
import json

class SNP(object):

    def __init__(self, soup, sourceCode):
        self.soup = soup
        self.sourceCode = sourceCode

    def browser_title(self):
        try:
            browserTitle = self.soup.title.string.strip()
        except:
            browserTitle = 'Not Present'

        return browserTitle

    def breadcrumb(self):
        breadcrumb_list = []
        try:
            divElement = self.soup.find('ol', {'class': 'breadcrumb'})
            liElements = divElement.find_all('li')
            for li in liElements:
                text = li.text.strip()
                breadcrumb_list.append(text)
        except:
            breadcrumb_list.append("Not Present")

        return breadcrumb_list

    def meta_description(self):
        try:
            metaDescription = self.soup.find("meta", {"name": "DESCRIPTION"})['content']
        except:
            metaDescription = "Not Present"

        return metaDescription

    def meta_keywords(self):
        try:
            metaKeywords = self.soup.find("meta", {"name": "KEYWORDS"})['content']
        except:
            metaKeywords = "Not Present"

        return metaKeywords

    def page_title(self):
        try:
            pageTitle = self.soup.find('h1', {'id': 'sharedPdPageProductTitle'}).text.strip()
        except:
            pageTitle = "Not Present"

        return pageTitle

    def hero_image_link(self):
        hero_image_list = []
        try:
            sectionElement = self.soup.find('section', {'id': 'hero-container'})
            imageElements = sectionElement.find_all('img')
            for imageElement in imageElements:
                image = imageElement.attrs['src']
                hero_image_list.append(image)
        except:
            hero_image_list.append('Not Present')

        return hero_image_list

    def hero_video(self):
        heroVideo = ""
        try:
            hero_video = self.soup.find('section', {'id': 'hero-container'})

            video = hero_video.find('input').attrs
            vcode = video['data-code']
            heroVideo = 'http://cf.c.ooyala.com/' + vcode + '/DOcJ-FxaFrRg4gtDEwOjYyOjBhOyD0Uk'

        except:
            heroVideo = "Not Present"

        return heroVideo

    def hero_description(self):
        try:
            spanElement = self.soup.find('span', {'class' : 'marketing-blurb'})
            heroDescription = spanElement.text.strip()
            return heroDescription
        except:
            return 'Not Present'

    def pricing(self):
        try:
            spanElement = self.soup.find('span', {'data-testid': 'sharedPSPDellPrice'})
            price = spanElement.text.strip()
            return price
        except:
            return 'Not Present'

    def tabs(self):
        tabs_list = []
        try:
            liElements = self.soup.find_all('li', {'class' : 'scroll-item'})
            for li in liElements:
                tab = li.text.strip()
                tabs_list.append(tab)
        except:
            tabs_list.append('Not Present')

        return tabs_list


    def features(self):
        features = {'title_alt' : []}
        try:

            FeatureImageList = self.sourceCode.split('FeatureImage')
            for x in range(1, len(FeatureImageList)):
                dict_title_alt = {}
                FeatureImageSoup = BeautifulSoup(FeatureImageList[x], 'lxml')
                try:
                    dict_title_alt['image_alt'] = FeatureImageSoup.find('img').attrs['alt']
                    dict_title_alt['image_link'] = FeatureImageSoup.find('img').attrs['data-original']
                except:
                    dict_title_alt['image_alt'] = 'Not Present'
                    dict_title_alt['image_link'] = 'Not Present'
                try:
                    dict_title_alt['feature_title'] = FeatureImageSoup.find('h2').text.strip()
                except:
                    dict_title_alt['feature_title'] = 'Not Present'
                features['title_alt'].append(dict_title_alt)

            FeatureTextList = self.sourceCode.split('FeatureText')
            for x in range(1, len(FeatureTextList)):
                dict_title_alt = {}
                FeatureTextSoup = BeautifulSoup(FeatureTextList[x], 'lxml')
                try:
                    dict_title_alt['image_alt'] = FeatureTextSoup.find('img').attrs['alt']
                    dict_title_alt['image_link'] = FeatureTextSoup.find('img').attrs['data-original']
                except:
                    dict_title_alt['image_alt'] = 'Not Present'
                    dict_title_alt['image_link'] = 'Not Present'
                try:
                    dict_title_alt['feature_title'] = FeatureTextSoup.find('h2').text.strip()
                except:
                    dict_title_alt['feature_title'] = 'Not Present'
                features['title_alt'].append(dict_title_alt)

            # Remaining Feature titles
            try:
                divElements = self.soup.find_all('div', {'class' : 'threeUp-image-content'})
                h3Elements =self.soup.find_all('h3', {'class' : 'threeUp-image-title'})
                count = 0
                for div in divElements:
                    dict_title_alt = {}

                    try:
                        dict_title_alt['image_alt'] = div.find('img').attrs['alt']
                        dict_title_alt['image_link'] = div.find('img').attrs['data-original']
                    except:
                        dict_title_alt['image_alt'] = 'Not Present'
                        dict_title_alt['image_link'] = 'Not Present'
                    try:
                        dict_title_alt['feature_title'] = h3Elements[count].text.strip()
                    except:
                        dict_title_alt['feature_title'] = 'Not Present'
                    features['title_alt'].append(dict_title_alt)
                    count = count + 1
            except:
                print('Nothing')



            return features
        except:
            return features



    def support(self):   #drivers, manuals and support
        support = {'image_links' :[],
                    'titles': [],
                    'descriptions': []
        }
        try:
            divElement = self.soup.find('div', {'id' : 'support-container'})
            imgTags = divElement.find_all('img')
            for imgTag in imgTags:
                src = imgTag.attrs['src']
                support['image_links'].append(src)

            divTag = divElement.find('div', {'class', 'col-xs-9'})
            h4Tag = divTag.find('h4')
            title = h4Tag.text.strip()
            support['titles'].append(title)

            pTags = divTag.find_all('p', {'class', 'bottom-offset-small'})
            for pTag in pTags:
                support['descriptions'].append(pTag.text.strip())

            return support
        except:
            return support

    def intelLogo(self):
        try:
            intelLogo = ''
            if "alt=\"Intel" in self.sourceCode:
                intelLogo = 'Present'
            else:
                intelLogo = 'Not Present'
            return intelLogo
        except:
            intelLogo = 'Not Present'
            return intelLogo

    def technote(self):
        technotes = []
        try:
            technoteDict = {}
            language = self.soup.find("meta", {"name": "LANGUAGE"})['content']
            country = self.soup.find("meta", {"name": "COUNTRY"})['content']
            #finding technotes
            technoteKeys = []
            aTags = self.soup.find_all('a', {'class' : 'technote'})
            for aTag in aTags:
                technoteKey = aTag.attrs['rel']
                print(technoteKey)
                technoteKey = technoteKey[0][technoteKey[0].find(':')+1:len(technoteKey[0])]
                technoteKeys.append(technoteKey)
            # forming url and get request to the url
            for technoteKey in technoteKeys:
                url = 'https://www.dell.com/csbapi/' + language + '-' + country + '/technote?techNoteKey=' + technoteKey
                responseObject = requests.get(url)
                sourceCode = responseObject.text
                jsonResponse = json.loads(sourceCode)
                print(jsonResponse['TechNoteKey'])
                print(jsonResponse['TechNoteText'])
                technoteDict[jsonResponse['TechNoteKey']] = jsonResponse['TechNoteText']
                technotes.append(technoteDict)

            return technotes


        except:
            return technotes
