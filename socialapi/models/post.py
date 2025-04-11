from pydantic import BaseModel

class UserPostIn(BaseModel):
    body:str

class UserPost(UserPostIn):
    id:int

class CommentIn(BaseModel):
    body:str
    post_id:int

class CommentOut(CommentIn):
    id:int 

class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[CommentOut]

{"post":{"id":0, "body":"my post"},
"comments": [{"id":2, "post_id":0, "body": "my comment"}]
}