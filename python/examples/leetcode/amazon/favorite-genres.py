"""
https://leetcode.com/discuss/interview-question/373006

Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user
has listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within
that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the
user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre
if he/she has listened to the same number of songs per each of the genres.

Example 1:

Input:
userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output: {
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}

Explanation:
David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
"""
import collections


class Solution1(object):
    """ brute force"""
    def favorite_genres(self, user_songs, song_genres):
        result = {}
        for user, us in user_songs.items():
            for genre, gs in song_genres.items():
                matches = set(us) & set(gs)
                if len(matches) >= 2:
                    result.setdefault(user, [])
                    result[user].append(genre)
        return result


class Solution2(object):
    def favorite_genres(self, userSongs, genreSongs):
        result = {}
        genre_m = {s: g for g in genreSongs for s in genreSongs[g]}
        for user, songs in userSongs.items():
            aggr = collections.Counter(genre_m[s] for s in songs if s in genre_m)   # {Rock: 1, Jazz: 2}
            max_cnt = max(aggr.values())
            result[user] = [s for s, cnt in aggr.items() if cnt == max_cnt]
        return result


userSongs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma": ["song5", "song6", "song7"]
}
songGenres = {
    "Rock": ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno": ["song2", "song4"],
    "Pop": ["song5", "song6"],
    "Jazz": ["song8", "song9"]
}

assert Solution1().favorite_genres(userSongs, songGenres) == {
    "David": ["Rock", "Techno"],
    "Emma": ["Pop"]
}

assert Solution2().favorite_genres(userSongs, songGenres) == {
    "David": ["Rock", "Techno"],
    "Emma": ["Pop"]
}
