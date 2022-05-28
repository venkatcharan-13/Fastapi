from .importss import *
from . import models, schemas
from .database import SessionLocal, engine, get_db
 

models.Base.metadata.create_all(bind=engine)

app=FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="#---SSDCHARANP API---# ",
    description='''  Framwork of Python
                HAI !!! This framework is just like an useraccount having 
                  userd etails and user posts and the comments for the post
                Here we can do CRUD (Create, Read , Update, Delete ) the data what ever you want
    ''',
    terms_of_service="https://fastapi.tiangolo.com/",
    version="0.1.0",
    openapi_url="/openapi.json"
)


while True:
    try:
        conn = psycopg2.connect(host='localhost',database='postgres',user='postgres', password='pragna',cursor_factory=RealDictCursor)
        Cursor=conn.cursor()
        print("database connection was succesfull")
        break
    except Exception as error:
        print("connection to database failed")
        print("error",error)
        time.sleep(2)


@app.get("/")
def root():
    return {"messageeee hai world"}


######  ####  ###### ####### USERS ####### ##### #### ###### 

@app.get("/users", tags=["USERS"])
def get_users(db: Session = Depends(get_db)):
    users= db.query(models.User).all()
    return {"data":users}

@app.post("/users",status_code= status.HTTP_201_CREATED, tags=["USERS"])
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    print(user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"data": new_user}


@app.get("/users/{id}", tags=["USERS"])
def get_users(id : int, db: Session = Depends(get_db)):
    user= db.query(models.User).filter(models.User.user_id== id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    return {"post_details": user}

@app.delete("/users/{id}",status_code= status.HTTP_204_NO_CONTENT, tags=["USERS"])
def delete_user(id : int,db: Session = Depends(get_db)):
     users= db.query(models.User).filter(models.User.user_id== id)
     if users.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
     users.delete(synchronize_session=False)
     db.commit()
     return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/users/{id}", tags=["USERS"])
def update_user(id:int, updateuser: schemas.User,db: Session = Depends(get_db)):
    user_query=db.query(models.User).filter(models.User.user_id== id)
    users=user_query.first()
    if users == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    user_query.update(updateuser.dict(), synchronize_session=False)
    db.commit()

    return {"data": updateuser}


######  ####  ###### ####### POSTS ####### ###### #### ######

@app.get("/posts", tags=["POSTS"])
def get_posts(db: Session= Depends(get_db)):
    posts=db.query(models.Post).all()
    return {"data":posts}

@app.post("/posts",status_code= status.HTTP_201_CREATED, tags=["POSTS"])
def create_posts(post: schemas.Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}



@app.get("/users_posts/{id}", tags=["POSTS"])
def get_posts(id : int, db: Session = Depends(get_db)):
    post= db.query(models.Post).filter(models.Post.user_id== id).all()
    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    return {"post_details": post}

@app.get("/get_one_post/{id}", tags=["POSTS"])
def get_one_post(id : int, db: Session = Depends(get_db)):
    post= db.query(models.Post).filter(models.Post.post_id== id).first()
    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    return {"post_details": post}

@app.delete("/posts/{id}",status_code= status.HTTP_204_NO_CONTENT, tags=["POSTS"])
def delete_post(id : int,db: Session = Depends(get_db)):
     post= db.query(models.Post).filter(models.Post.user_id== id)
     if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
     post.delete(synchronize_session=False)
     db.commit()
     return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}", tags=["POSTS"])
def update_post(id:int, updatepost: schemas.Post,db: Session = Depends(get_db)):
    post_query=db.query(models.Post).filter(models.Post.post_id== id)
    post=post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    post_query.update(updatepost.dict(), synchronize_session=False)
    db.commit()

    return {"data": updatepost}


######  ####  ###### ####### COMMENTS ####### ###### #### ######

@app.get("/comments", tags=["COMMENTS"])
def get_posts(db: Session = Depends(get_db)):
    posts= db.query(models.Comments).all()
    return {"data":posts}

@app.post("/comments",status_code= status.HTTP_201_CREATED, tags=["COMMENTS"])
def create_comments(comments: schemas.Comments, db: Session = Depends(get_db)):
    new_comment = models.Comments(**comments.dict())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return {"data": new_comment}

@app.get("/posts_comments/{id}", tags=["COMMENTS"])
def get_one_comments(id : int, db: Session = Depends(get_db)):
    comment= db.query(models.Comments).filter(models.Comments.post_id== id).all()
    if not comment:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    return {"comment_details": comment}

@app.get("/get_one_comments/{id}", tags=["COMMENTS"])
def get_one_comments(id : int, db: Session = Depends(get_db)):
    comment= db.query(models.Comments).filter(models.Comments.comments_id== id).all()
    if not comment:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    return {"comment_details": comment}

@app.delete("/comments/{id}",status_code= status.HTTP_204_NO_CONTENT, tags=["COMMENTS"])
def delete_comments(id : int,db: Session = Depends(get_db)):
     comments= db.query(models.Comments).filter(models.Comments.comments_id== id)
     if comments.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
     comments.delete(synchronize_session=False)
     db.commit()
     return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/comments/{id}", tags=["COMMENTS"])
def update_comment(id:int, updatecomment: schemas.Comments,db: Session = Depends(get_db)):
    comments_query=db.query(models.Comments).filter(models.Comments.comments_id== id)
    comments=comments_query.first()
    if comments == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    comments_query.update(updatecomment.dict(), synchronize_session=False)
    db.commit()

    return {"data": updatecomment}




