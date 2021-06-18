import requests
import json

baseUrl = "https://my-json-server.typicode.com/typicode/demo/"
postEndpoint = "posts"

payload = {}
headers = {}

postsResponse = requests.request("GET", baseUrl + "posts", headers=headers, data=payload)
postList = json.loads(postsResponse.text)

commentsResponse = requests.request("GET", baseUrl + "comments", headers=headers, data=payload)
commentsList = json.loads(commentsResponse.text)

for post in postList:
    for comment in commentsList:
        if comment.get("postId") == post.get("id"):
            postComments = post.get("comments")
            if postComments is None:
                post["comments"] = []
            postComments = post.get("comments")
            postComments.append(comment)
print(postList)
