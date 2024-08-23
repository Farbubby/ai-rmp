import requests
from bs4 import BeautifulSoup

def scrape_rmp_link(link: str) -> dict[str, str | list[str]]:
    html = requests.get(link).text
    soup = BeautifulSoup(html, 'html.parser')

    rating = "N/A"
    num_ratings = "N/A"
    prof_name = "N/A"
    prof_dept = "N/A"
    university_name = "N/A"
    difficulty = "N/A"
    would_take_again = "N/A"
    classes_taught = []
    top_tags = []
    recent_comments = []

    # Get the relevant information
    # If the information is not found, the default value is "N/A" or []

    if (soup.find("div", class_="RatingValue__Numerator-qw8sqy-2 liyUjw")):
        rating = soup.find("div", class_="RatingValue__Numerator-qw8sqy-2 liyUjw").text + "/5"

    if (soup.find("div", class_="RatingValue__NumRatings-qw8sqy-0 jMkisx")):
        if (soup.find("div", class_="RatingValue__NumRatings-qw8sqy-0 jMkisx").find("a", class_=None)):
            num_ratings = soup.find("div", class_="RatingValue__NumRatings-qw8sqy-0 jMkisx").find("a", class_=None).text

    if (soup.find("div", class_="NameTitle__Name-dowf0z-0 cfjPUG")):
        prof_name = soup.find("div", class_="NameTitle__Name-dowf0z-0 cfjPUG").text

    if (soup.find("a", class_="TeacherDepartment__StyledDepartmentLink-fl79e8-0 iMmVHb")):
        prof_dept = soup.find("a", class_="TeacherDepartment__StyledDepartmentLink-fl79e8-0 iMmVHb").text

    if (soup.find("div", class_="NameTitle__Title-dowf0z-1 iLYGwn")):
        if (soup.find("div", class_="NameTitle__Title-dowf0z-1 iLYGwn").find("a", class_=None)):
            university_name = soup.find("div", class_="NameTitle__Title-dowf0z-1 iLYGwn").find("a", class_=None).text
    
    if (len(soup.find_all("div", class_="FeedbackItem__FeedbackNumber-uof32n-1 kkESWs")) > 1):
        would_take_again = soup.find_all("div", class_="FeedbackItem__FeedbackNumber-uof32n-1 kkESWs")[0].text
        difficulty = soup.find_all("div", class_="FeedbackItem__FeedbackNumber-uof32n-1 kkESWs")[1].text + "/5"

    classes_taught = []
    if (len(soup.find_all("div", class_="RatingHeader__StyledClass-sc-1dlkqw1-3 eXfReS")) > 0):
        classes = soup.find_all("div", class_="RatingHeader__StyledClass-sc-1dlkqw1-3 eXfReS")
        cache = {}
        for i in range(len(classes)):
            if classes[i].text not in cache:
                cache[classes[i].text] = 1
                classes_taught.append(classes[i].text)

    top_tags = []
    if (soup.find("div", class_="TeacherTags__TagsContainer-sc-16vmh1y-0 dbxJaW")):
        if (len(soup.find("div", class_="TeacherTags__TagsContainer-sc-16vmh1y-0 dbxJaW").find_all("span", class_="Tag-bs9vf4-0 hHOVKF")) > 0):
            tags = soup.find("div", class_="TeacherTags__TagsContainer-sc-16vmh1y-0 dbxJaW").find_all("span", class_="Tag-bs9vf4-0 hHOVKF")
            for i in range(len(tags)):
                top_tags.append(tags[i].text)


    recent_comments = []
    if (len(soup.find_all("div", class_="Comments__StyledComments-dzzyvm-0 gRjWel")) > 0):
        comments = soup.find_all("div", class_="Comments__StyledComments-dzzyvm-0 gRjWel")
        for i in range(len(comments)):
            recent_comments.append(comments[i].text)

    # Print the information
    print("\n[Professor Info]\n")

    print("Overall rating -", rating)
    print("Number of ratings -", num_ratings)
    print("Professor name -", prof_name)
    print("Professor department -", prof_dept)
    print("University name -", university_name)
    print("Level of difficulty -", difficulty)
    print("Would take again -", would_take_again)
    print("Classes taught -", classes_taught)
    print("Top tags -", top_tags)
    print("Recent comments -", recent_comments)

    print()

    # Return the information as a dictionary 
    # {
    #     "rating": str,
    #     "num_ratings": str,
    #     "prof_name": str,
    #     "prof_dept": str,
    #     "university_name": str,
    #     "difficulty": str,
    #     "would_take_again": str,
    #     "classes_taught": str[],
    #     "top_tags": str[],
    #     "comments": str[]
    # }

    result = {"rating": rating,
              "num_ratings": num_ratings,
              "prof_name": prof_name,
              "prof_dept": prof_dept,
              "university_name": university_name,
              "difficulty": difficulty,
              "would_take_again": would_take_again,
              "classes_taught": classes_taught,
              "top_tags": top_tags,
              "comments": recent_comments}
    
    return result
