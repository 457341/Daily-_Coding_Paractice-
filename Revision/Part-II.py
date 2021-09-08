# ? Question
# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
# ! Answer
# def foo(data):
#     if len(data) == len(set(data)):
#         return True
#     else:
#         return False
# print(foo([1,2,3]))
# print(foo([1,1,3, 4, 5, 6, 7]))
#? Question
# Write a Python program to count the number of each character of a given text of a text file.
# f = open("text.txt", "r")
# print(f.read())
# str = "My name is manzoor"
# str = str.split()
# for s in str:
#     s = s.split()
#     print(s)
# print(str)
#! Answer

# def remove_nums(int_list):
  #list starts with 0 index
  # position = 3 - 1 
  # idx = 0
  # len_list = (len(int_list))
#   while len_list>0:
#     idx = (position+idx)%len_list
#     print(int_list.pop(idx))
#     len_list -= 1
# nums = [10,20,30,40,50,60,70,80,90]
# remove_nums(nums)
#? Question
# Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers.
#! Answer
# def three_sum(nums):
#   result = []
#   nums.sort()
#   for i in range(len(nums)-2):
#     if i> 0 and nums[i] == nums[i-1]:
#       continue
#     l, r = i+1, len(nums)-1
#     while l < r:
#       s = nums[i] + nums[l] + nums[r]
#       if s > 0:
#         r -= 1
#       elif s < 0:
#           l += 1
#       else:
#         # found three sum
#         result.append((nums[i], nums[l], nums[r]))
#         # remove duplicates
#         while l < r and nums[l] == nums[l+1]:
#           l+=1
#           while l < r and nums[r] == nums[r-1]:
#             r -= 1
#             l += 1
#             r -= 1
#           return result

# x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
# print(three_sum(x))
#? Question
# Write a Python program to get the top stories from Google news.
#! Answer
# import bs4
# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen

# news_url="https://news.google.com/news/rss"
# Client=urlopen(news_url)
# xml_page=Client.read()
# Client.close()

# soup_page=soup(xml_page,"xml")
# news_list=soup_page.findAll("item")
# Print news title, url and publish date
# for news in news_list:
#   print(news.title.text)
#   print(news.link.text)
#   print(news.pubDate.text)
#   print("-"*60)


#? Question
# Write a Python program to get a list of locally installed Python modules.
#! Answer
# import pkg_resources
# installed_packages = pkg_resources.working_set
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
#      for i in installed_packages])
# for m in installed_packages_list:
#     print(m)
#? Question 
# Write a Python program to display some information about the OS where the script is running.
#! Answer
import platform as pl

os_profile = [
        'architecture',
        'linux_distribution',
        'mac_ver',
        'machine',
        'node',
        'platform',
        'processor',
        'python_build',
        'python_compiler',
        'python_version',
        'release',
        'system',
        'uname',
        'version',
    ]
for key in os_profile:
  if hasattr(pl, key):
    print(key +  ": " + str(getattr(pl, key)()))
