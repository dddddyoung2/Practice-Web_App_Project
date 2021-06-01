from spotify_app import db


class Audio(db.Model):
    __tablename__ = 'audio'

    danceability = db.Column(db.FLOAT)
    energy = db.Column(db.FLOAT)
    acousticness = db.Column(db.FLOAT)
    instrumentalness = db.Column(db.FLOAT)
    valence = db.Column(db.FLOAT)
    track_id = db.Column(db.VARCHAR, primary_key=True)

    playlists= db.relationship('Playlist', backref= 'audio', cascade = "all, delete")

    def __repr__(self):
        return f"Audio feature {self.track_id}"


    # def __repr__(self):
    #     d = f"danceability: {self.danceability}"
    #     e = f"energy: {self.energy}"
    #     a = f"acousticness: {self.acousticness}"
    #     i = f"instrumentalness: {self.instrumentalness}"
    #     v = f"valence: {self.valence}"
    #     return d,e,a,i,v



    