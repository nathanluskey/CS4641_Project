"""
Code for getting features from 'compiledGenreData_MissingAttributes.csv'
analysis_sample_rate,artist_7digitalid,artist_familiarity,artist_hotttnesss,artist_id,artist_latitude,artist_location,artist_longitude,artist_mbid,artist_mbtags,artist_mbtags_count,artist_name,artist_playmeid,artist_terms,artist_terms_freq,artist_terms_weight,audio_md5,bars_confidence,bars_start,beats_confidence,beats_start,danceability,duration,end_of_fade_in,energy,key,key_confidence,loudness,mode,mode_confidence,release,release_7digitalid,sections_confidence,sections_start,segments_confidence,segments_loudness_max,segments_loudness_max_time,segments_loudness_start,segments_pitches,segments_start,segments_timbre,similar_artists,song_hotttnesss,song_id,start_of_fade_out,tatums_confidence,tatums_start,tempo,time_signature,time_signature_confidence,title,track_7digitalid,track_id,year,genre
"""

import pandas

csv_file = pandas.read_csv('compiledGenreData_MissingAttributes.csv')

def get_num_songs():
    return len(csv_file)

def get_analysis_sample_rate(idx):
    return csv_file['analysis_sample_rate'][idx]

def get_artist_7digitalid(idx):
    return csv_file['artist_7digitalid'][idx]

def get_artist_familiarity(idx):
    return csv_file['artist_familiarity'][idx]
    
def get_artist_hotttnesss(idx):
    return csv_file['artist_hotttnesss'][idx]

def get_artist_id(idx):
    return csv_file['artist_id'][idx]
    
def get_artist_latitude(idx):
    return csv_file['artist_latitude'][idx]

def get_artist_location(idx):
    return csv_file['artist_location'][idx]

def get_artist_longitude(idx):
    return csv_file['artist_longitude'][idx]

def get_artist_mbid(idx):
    return csv_file['artist_mbid'][idx]

def get_artist_mbtags(idx):
    return csv_file['artist_mbtags'][idx]

def get_artist_mbtags_count(idx):
    return csv_file['artist_mbtags_count'][idx]

def get_artist_name(idx):
    return csv_file['artist_name'][idx]

def get_artist_playmeid(idx):
    return csv_file['artist_playmeid'][idx]

def get_artist_terms(idx):
    return csv_file['artist_terms'][idx]

def get_artist_terms_freq(idx):
    return csv_file['artist_terms_freq'][idx]

def get_artist_terms_weight(idx):
    return csv_file['artist_terms_weight'][idx]

def get_audio_md5(idx):
    return csv_file['audio_md5'][idx]

def get_bars_confidence(idx):
    return csv_file['bars_confidence'][idx]

def get_bars_start(idx):
    return csv_file['bars_start'][idx]

def get_beats_confidence(idx):
    return csv_file['beats_confidence'][idx]

def get_beats_start(idx):
    return csv_file['beats_start'][idx]

def get_danceability(idx):
    return csv_file['danceability'][idx]

def get_duration(idx):
    return csv_file['duration'][idx]

def get_end_of_fade_in(idx):
    return csv_file['end_of_fade_in'][idx]

def get_energy(idx):
    return csv_file['energy'][idx]

def get_key(idx):
    return csv_file['key'][idx]

def get_key_confidence(idx):
    return csv_file['key_confidence'][idx]

def get_loudness(idx):
    return csv_file['loudness'][idx]

def get_mode(idx):
    return csv_file['mode'][idx]

def get_mode_confidence(idx):
    return csv_file['mode_confidence'][idx]

def get_release(idx):
    return csv_file['release'][idx]

def get_release_7digitalid(idx):
    return csv_file['release_7digitalid'][idx]

def get_sections_confidence(idx):
    return csv_file['sections_confidence'][idx]

def get_sections_start(idx):
    return csv_file['sections_start'][idx]

def get_segments_confidence(idx):
    return csv_file['segments_confidence'][idx]

def get_segments_loudness_max(idx):
    return csv_file['segments_loudness_max'][idx]

def get_segments_loudness_max_time(idx):
    return csv_file['segments_loudness_max_time'][idx]

def get_segments_loudness_start(idx):
    return csv_file['segments_loudness_start'][idx]

def get_segments_pitches(idx):
    return csv_file['segments_pitches'][idx]

def get_segments_start(idx):
    return csv_file['segments_start'][idx]

def get_segments_timbre(idx):
    return csv_file['segments_timbre'][idx]

def get_similar_artists(idx):
    return csv_file['similar_artists'][idx]

def get_song_hotttnesss(idx):
    return csv_file['song_hotttnesss'][idx]

def get_song_id(idx):
    return csv_file['song_id'][idx]

def get_start_of_fade_out(idx):
    return csv_file['start_of_fade_out'][idx]

def get_tatums_confidence(idx):
    return csv_file['tatums_confidence'][idx]

def get_tatums_start(idx):
    return csv_file['tatums_start'][idx]

def get_tempo(idx):
    return csv_file['tempo'][idx]

def get_time_signature(idx):
    return csv_file['time_signature'][idx]

def get_time_signature_confidence(idx):
    return csv_file['time_signature_confidence'][idx]

def get_title(idx):
    return csv_file['title'][idx]

def get_track_7digitalid(idx):
    return csv_file['track_7digitalid'][idx]

def get_track_id(idx):
    return csv_file['track_id'][idx]

def get_year(idx):
    return csv_file['year'][idx]

def get_genre(idx):
    return csv_file['genre'][idx]


