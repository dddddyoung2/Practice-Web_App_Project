def msg_processor(msg_code):
    '''
    msg_processor returns a msg object with 'msg', 'type'
    where 'msg' corresponds to the message user sees
    and 'type' is the color of the alert element

    codes:
        - 0 : Successfully added to database
        - 1 : User does not exist
        - 2 : Unable to retrieve tweets
        - 3 : Successfully deleted user
                - 4 : 해당 이름을 가진 가수의 곡 정보가 없습니다. 다른 곡을 검색해 보세요. 
                - 5 : 가수의 이름을 입력하세요.
                - 6 : 곡명을 입력하세요.
    '''

    msg_code = int(msg_code)

    msg_list = [
        (
            'Successfully added to database',
            'success'
        ),
        (
            'User does not exist',
            'warning'
        ),
        (
            'Unable to retrieve tweets',
            'warning'
        ),
        (
            'Successfully deleted user',
            'info'
        ),
                (
                    '해당 이름을 가진 가수의 곡 정보가 없습니다. 다른 곡을 검색해 보세요.',
                    'warning'
                ),
                (
                    '가수의 이름을 입력하세요.',
                    'warning'
                ),
                (
                    '곡명을 입력하세요.',
                    'warning'
                )
    ]


    return {
        'msg':msg_list[msg_code][0],
        'type':msg_list[msg_code][1]
    }

def predict_text(user_list, predict_text):
    user_1, user_2 = user_list

    embeddings = []
    labels = []

    for tw in user_1.tweets:
        embeddings.append(tw.embedding)
        labels.append(user_1.username)

    for tw in user_2.tweets:
        embeddings.append(tw.embedding)
        labels.append(user_2.username)

    classifier = LogisticRegression()
    classifier.fit(embeddings, labels)

    predict_embedding = en.encode(texts=[predict_text])
    prediction = classifier.predict(predict_embedding)

    print(f"Prediction Results {prediction[0]}")

    return prediction[0]
