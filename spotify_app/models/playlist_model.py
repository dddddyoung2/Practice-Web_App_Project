from spotify_app import db

class Playlist(db.Model):
    __tablename__ = 'playlist'

    artist_id = db.Column(db.VARCHAR, primary_key=True)
    artist_name = db.Column(db.VARCHAR, nullable=False)
    track_id = db.Column(db.VARCHAR, db.ForeignKey('audio.track_id'))
    track_name = db.Column(db.VARCHAR, nullable=False)
    popularity = db.Column(db.Integer)
    images = db.Column(db.VARCHAR)

    
    
    def __repr__(self):
        return f"Song {self.id}"