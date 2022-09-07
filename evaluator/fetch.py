import requests
from time import sleep
from parsel import Selector
from .face_detection import FaceDetector

def single_fetch_content(github_user):
    git_url = "https://github.com/" + github_user
    readme_url = "https://github.com/" + github_user + "/" + github_user

    git_response = requests.get(git_url)
    readme_response = requests.get(readme_url)

    user_dic = dict()

    user_dic['github_username'] = github_user

    user_dic["github"] = Selector(
            text=git_response.text
        )

    user_dic["github_readme"] = Selector(
            text=readme_response.text
        )

    photo_url = user_dic["github"].css('a[itemprop="image"]::attr(href)').get()



    if not bool(photo_url):
        photo_url = 'https://i.imgur.com/PRiA9r9.png'
    

    photo_response = requests.get(photo_url)

    with open("evaluator/static/photos/" + github_user + "_image.jpg", "wb") as handler:
        handler.write(photo_response.content)
        user_dic["photo"] = FaceDetector.find_faces("evaluator/static/photos/" + github_user + "_image.jpg")

    return user_dic


# def group_fetch_content(list_of_dicts):
#     git_urls = [
#         "https://github.com/" + each_dict["github_username"]
#         for each_dict in list_of_dicts
#     ]
#     readme_urls = [
#         "https://github.com/"
#         + each_dict["github_username"]
#         + "/"
#         + each_dict["github_username"]
#         for each_dict in list_of_dicts
#     ]

#     git_gen = (grequests.get(git) for git in git_urls)
#     readme_gen = (grequests.get(readme) for readme in readme_urls)

#     git_responses = grequests.map(git_gen)
#     readme_responses = grequests.map(readme_gen)

#     sleep(1)

#     for index in range(len(list_of_dicts)):
#         list_of_dicts[index]["github"] = Selector(
#             text=git_responses[index].text
#         )
#         list_of_dicts[index]["github_readme"] = Selector(
#             text=readme_responses[index].text
#         )

#     sleep(1)

#     photos_urls = [
#         selector["github"].css('a[itemprop="image"]::attr(href)').get()
#         for selector in list_of_dicts
#     ]

#     for index in range(len(photos_urls)):
#         if not bool(photos_urls[index]):
#             photos_urls[index] = 'https://i.imgur.com/PRiA9r9.png'
    

#     photo_gen = (grequests.get(photo) for photo in photos_urls)
#     photo_responses = grequests.map(photo_gen)

#     sleep(1)

#     for index in range(len(list_of_dicts)):
#         with open(
#             "photos/" + list_of_dicts[index]["github_username"] + "_image.jpg",
#             "wb",
#         ) as handler:
#             handler.write(photo_responses[index].content)
#         list_of_dicts[index]["photo"] = FaceDetector.find_faces(
#             "photos/" + list_of_dicts[index]["github_username"] + "_image.jpg"
#         )

#     return list_of_dicts