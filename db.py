from datetime import datetime

comments = {
    1: {
        "image_id": 9999,
        "user_id": 202920920,
        "commentBody": "I think this photo is wonderful, possibly one of my favoruites",
        "created_at": datetime.now()
    },
    2: {
        "image_id": 9999,
        "user_id": 202920920,
        "commentBody": "I think this photo is terrible",
        "created_at": datetime.now()
    }
}

reactions = {
    1: {
        "comment_id": 1,
        "user_id": 9202920292,
        "type": 'like'
    }
}

images = {
    1: {
        "user_id": 9292929292,
        "image_url": 'Whaat test.com'
    }
}
