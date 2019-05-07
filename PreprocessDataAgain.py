import os
import re
metafile = "Res_reviews/output_meta_yelpResData_NRYRcleaned.txt"
reviewfile = "Res_reviews/output_review_yelpResData_NRYRcleaned.txt"

def processReview(review):
    b = ",./\'\":;()!$&%*#"
    for char in b:
        review = review.replace(char, "")

    return review

def processLine(metaline, reviewline):
    splitline = metaline.split(' ')
    datelist = splitline[0].split('/')
    month = datelist[0]
    date = datelist[1]
    year= datelist[2]
    reviewid = splitline[1]
    reviewerid = splitline[2]
    productid = splitline[3]
    rating1 = splitline[5]
    rating2 = splitline[6]
    rating3 = splitline[7]
    rating4 = splitline[8]
    review = processReview(reviewline)
    label = splitline[4]
    csvobj.write(month+','+date+','+year+','+reviewid+',' +reviewerid+','+ productid+',' +rating1+','+ rating2+','+rating3+','+rating4+','+review+','+label+'\n')


csvobj = open("Res_reviews/ReviewCSV.txt", "w")
csvobj.write("month, date, year, reviewid, reviewerid, productid, rating1, rating2, rating3, rating4, review, label\n")


with open(metafile) as xh:
  with open(reviewfile) as yh:
      xlines = xh.readlines()
      ylines = yh.readlines()
      for i in range(len(xlines)):
        metaline = xlines[i].strip()
        reviewline = ylines[i].strip()
        processLine(metaline,reviewline)





