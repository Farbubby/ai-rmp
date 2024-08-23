import requests
from bs4 import BeautifulSoup

def scrape_rmp_link(link: str) -> dict:
    html = requests.get(link).text
    soup = BeautifulSoup(html, 'html.parser')

    # Get the relevant information
    rating = soup.find_all("div", class_="RatingValue__Numerator-qw8sqy-2 liyUjw")[0].text + "/5"

    num_ratings = soup.find_all("div", class_="RatingValue__NumRatings-qw8sqy-0 jMkisx")[0].find_all("a", class_=None)[0].text

    prof_name = soup.find_all("div", class_="NameTitle__Name-dowf0z-0 cfjPUG")[0].text

    prof_dept = soup.find_all("a", class_="TeacherDepartment__StyledDepartmentLink-fl79e8-0 iMmVHb")[0].text

    university_name = soup.find_all("div", class_="NameTitle__Title-dowf0z-1 iLYGwn")[0].find_all("a", class_=None)[0].text

    difficulty = soup.find_all("div", class_="FeedbackItem__FeedbackNumber-uof32n-1 kkESWs")[1].text + "/5"

    would_take_again = soup.find_all("div", class_="FeedbackItem__FeedbackNumber-uof32n-1 kkESWs")[0].text

    classes = soup.find_all("div", class_="RatingHeader__StyledClass-sc-1dlkqw1-3 eXfReS")
    classes_taught = []
    cache = {}
    for i in range(len(classes)):
        if classes[i].text not in cache:
            cache[classes[i].text] = 1
            classes_taught.append(classes[i].text)

    tags = soup.find_all("div", class_="TeacherTags__TagsContainer-sc-16vmh1y-0 dbxJaW")[0].find_all("span", class_="Tag-bs9vf4-0 hHOVKF")
    top_tags = []
    for i in range(len(tags)):
        top_tags.append(tags[i].text)

    comments = soup.find_all("div", class_="Comments__StyledComments-dzzyvm-0 gRjWel")
    recent_comments = []
    for i in range(10):
        if i == len(comments):
            break
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
    #     "recent_comments": str[]
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
              "recent_comments": recent_comments}
    
    print(result)
    return "ok"

scrape_rmp_link("https://www.ratemyprofessors.com/professor/900614")
