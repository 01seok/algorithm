def solution(genres, plays):
    answer = []

    # 장르별 총 재생 횟수 구하고
    # 장르별 노래 리스트 넣고
    # 장르 총 재생 횟수 기준으로 내림차순
    # 장르에서 2곡 고르는데 재생횟수는 내림차순, 고유번호는 오름차순 -> 음수 부호

    genre_total_play = {}
    for song_num in range(len(genres)):
        # 처음 들어오는 장르라면
        if genres[song_num] not in genre_total_play:
            genre_total_play[genres[song_num]] = 0
        genre_total_play[genres[song_num]] += plays[song_num]

    genre_songs = {}
    for song in range(len(genres)):
        if genres[song] not in genre_songs:
            genre_songs[genres[song]] = []
        # 인덱스랑 재생횟수 같이 넣기
        genre_songs[genres[song]].append((song, plays[song]))

    # 장르별 총 재생횟수 내림차순 정렬
    sorted_genres = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)

    for genre, i in sorted_genres:
        # 장르 내에서 재생 횟수는 내림차순으로, 인덱스는 오름차순으로 정렬
        songs = sorted(genre_songs[genre], key=lambda x: (-x[1], x[0]))

        for i in range(min(2, len(songs))):
            answer.append(songs[i][0])

    return answer