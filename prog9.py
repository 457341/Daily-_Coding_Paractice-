# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014
exam_st_date = (11, 12, 2014)
new_date_format = str(exam_st_date[0]) + " / " + str(exam_st_date [1]) + " / " +str( exam_st_date[2]) 
print(new_date_format)


# From below it extra information, problem solved upper
color_list = ("Red","Green","White" ,"Black")
print( "%s %s"%(color_list[0],color_list[-1]))

# different ways to print 
exam_st_date = (11, 12, 2014)
print("%i %i %i"%exam_st_date) # if you want to print all
print("%i %i "%(exam_st_date[0],exam_st_date[-1])) # if you want to print some specific