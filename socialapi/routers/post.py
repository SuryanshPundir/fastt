

from fastapi import APIRouter, HTTPException

from socialapi.models.post import UserPost, UserPostIn, CommentOut, CommentIn

router = APIRouter()


post_datadict={}
comment_table={}

def find_post(post_id: int):
    return post_datadict.get(post_id)

@router.post("/post", response_model=UserPost)
async def create_post(post: UserPostIn):
    data=post.model_dump()
    last_record_id  = len(post_datadict)
    new_post= {**data, "id": last_record_id}
    post_datadict[last_record_id]= new_post
    return new_post

@router.get("/post", response_model=list[UserPost])
async def get_all_posts():
    return list(post_datadict.values())

@router.post("/comment", response_model=CommentOut)
async def create_comment(comment: CommentIn):
    post=find_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    data=comment.model_dump()
    last_record_id  = len(comment_table)
    new_comment= {**data, "id": last_record_id}
    post_datadict[last_record_id]= new_comment
    return new_comment

@router.get("/post/{post_id}/comment", response_model=list[CommentOut])
async def get_comments_on_post(post_id:int):
    return[
        comment for comment in comment_table.values() if comment["post_id"]==post_id
    ]

