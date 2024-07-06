# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 12:50:47 2023

@author: Python Desk
"""


# import youtube_dl

# def download_course(course_url, email, password):
#     """Downloads a course from YouTube using youtube_dl."""
#     options = {
#         'email': email,
#         'password': password,
#     }
#     with youtube_dl.YoutubeDL(options) as ydl:
#         ydl.download([course_url])

# if __name__ == '__main__':
#     course_url = 'https://www.udemy.com/course/python-js-react-blockchain/learn/lecture/16602664#questions'
#     email = 'sreeforall.polimera@gmail.com'
#     password = '$ReeR$2411'
#     download_course(course_url, email, password)


import yt_dlp

def download_udemy_course(course_url):
    """Downloads an Udemy course using yt-dlp."""
    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'outtmpl': '%(playlist)s/%(chapter)s/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([course_url])

if __name__ == '__main__':
    course_url = 'https://www.udemy.com/course/python-js-react-blockchain/learn/lecture/16602664#questions'
    download_udemy_course(course_url)