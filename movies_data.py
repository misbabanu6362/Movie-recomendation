# ── Genre Explorer — Movie Dataset ───────────────────────────────────────────
# Fields: title, language, genres (list), year, rating (out of 10), description
# Genres used: Action, Drama, Comedy, Romance, Sci-Fi, Thriller,
#              Crime, Biography, Mystery, Horror, Music, Sport, History, Adventure
# ─────────────────────────────────────────────────────────────────────────────

MOVIES = [

    # ═══════════════════════════════════════════════════════════════════════════
    # ENGLISH MOVIES (20)
    # ═══════════════════════════════════════════════════════════════════════════
    {"title": "The Dark Knight",           "language": "English", "year": 2008, "rating": 9.0,
     "genres": ["Action", "Crime", "Drama"],
     "desc": "Batman faces the Joker, a criminal mastermind who plunges Gotham City into chaos."},

    {"title": "Inception",                 "language": "English", "year": 2010, "rating": 8.8,
     "genres": ["Action", "Sci-Fi", "Thriller"],
     "desc": "A thief enters people's dreams to steal secrets hidden deep in their subconscious."},

    {"title": "Interstellar",              "language": "English", "year": 2014, "rating": 8.7,
     "genres": ["Sci-Fi", "Drama", "Adventure"],
     "desc": "Astronauts travel through a wormhole near Saturn in search of a new home for humanity."},

    {"title": "The Matrix",                "language": "English", "year": 1999, "rating": 8.7,
     "genres": ["Action", "Sci-Fi"],
     "desc": "A hacker discovers reality is a simulation and joins a war against the machines."},

    {"title": "Avengers: Endgame",         "language": "English", "year": 2019, "rating": 8.4,
     "genres": ["Action", "Adventure", "Sci-Fi"],
     "desc": "Earth's mightiest heroes assemble one last time to undo Thanos's snap."},

    {"title": "Forrest Gump",              "language": "English", "year": 1994, "rating": 8.8,
     "genres": ["Drama", "Romance", "Sport"],
     "desc": "A kind-hearted Alabama man witnesses and influences pivotal American historical events."},

    {"title": "The Shawshank Redemption",  "language": "English", "year": 1994, "rating": 9.3,
     "genres": ["Drama", "Crime"],
     "desc": "A wrongly convicted banker forges an enduring friendship inside Shawshank prison."},

    {"title": "Pulp Fiction",              "language": "English", "year": 1994, "rating": 8.9,
     "genres": ["Crime", "Drama", "Thriller"],
     "desc": "Interlocking stories of hitmen, gangsters, and a boxer in Los Angeles."},

    {"title": "The Godfather",             "language": "English", "year": 1972, "rating": 9.2,
     "genres": ["Crime", "Drama"],
     "desc": "The Corleone crime family navigates power, loyalty, and betrayal across generations."},

    {"title": "Titanic",                   "language": "English", "year": 1997, "rating": 7.9,
     "genres": ["Drama", "Romance", "History"],
     "desc": "A star-crossed romance blooms aboard the ill-fated RMS Titanic."},

    {"title": "Avatar",                    "language": "English", "year": 2009, "rating": 7.9,
     "genres": ["Action", "Adventure", "Sci-Fi"],
     "desc": "A marine bonds with the Na'vi people of the alien moon Pandora to protect their world."},

    {"title": "Gladiator",                 "language": "English", "year": 2000, "rating": 8.5,
     "genres": ["Action", "Adventure", "Drama"],
     "desc": "A betrayed Roman general fights his way through the gladiator arena to avenge his family."},

    {"title": "The Silence of the Lambs",  "language": "English", "year": 1991, "rating": 8.6,
     "genres": ["Crime", "Thriller", "Horror"],
     "desc": "An FBI trainee enlists the brilliant-but-murderous Hannibal Lecter to catch a serial killer."},

    {"title": "Get Out",                   "language": "English", "year": 2017, "rating": 7.7,
     "genres": ["Horror", "Mystery", "Thriller"],
     "desc": "A visit to his girlfriend's family reveals terrifying secrets for a young Black man."},

    {"title": "Whiplash",                  "language": "English", "year": 2014, "rating": 8.5,
     "genres": ["Drama", "Music"],
     "desc": "A young drummer is pushed to his absolute limits by an obsessive, demanding instructor."},

    {"title": "La La Land",                "language": "English", "year": 2016, "rating": 8.0,
     "genres": ["Drama", "Music", "Romance"],
     "desc": "A jazz pianist and an aspiring actress fall in love while chasing their dreams in LA."},

    {"title": "The Wolf of Wall Street",   "language": "English", "year": 2013, "rating": 8.2,
     "genres": ["Biography", "Comedy", "Crime"],
     "desc": "Jordan Belfort's wild rise through Wall Street greed, fraud, and excess."},

    {"title": "Joker",                     "language": "English", "year": 2019, "rating": 8.4,
     "genres": ["Crime", "Drama", "Thriller"],
     "desc": "A failed comedian's descent into madness gives birth to Gotham's most iconic villain."},

    {"title": "Parasite",                  "language": "English", "year": 2019, "rating": 8.5,
     "genres": ["Comedy", "Drama", "Thriller"],
     "desc": "A poor Korean family infiltrates a wealthy household with darkly comic results."},

    {"title": "Doctor Strange",            "language": "English", "year": 2016, "rating": 7.5,
     "genres": ["Action", "Adventure", "Sci-Fi"],
     "desc": "A surgeon discovers the mystic arts and battles threats across alternate dimensions."},

    # ═══════════════════════════════════════════════════════════════════════════
    # HINDI (BOLLYWOOD) MOVIES (15)
    # ═══════════════════════════════════════════════════════════════════════════
    {"title": "3 Idiots",                  "language": "Hindi", "year": 2009, "rating": 8.4,
     "genres": ["Comedy", "Drama"],
     "desc": "Three engineering students rebel against rote learning and discover their true passions."},

    {"title": "Dangal",                    "language": "Hindi", "year": 2016, "rating": 8.4,
     "genres": ["Biography", "Drama", "Sport"],
     "desc": "A wrestler father trains his daughters to become world-champion wrestlers."},

    {"title": "PK",                        "language": "Hindi", "year": 2014, "rating": 8.1,
     "genres": ["Comedy", "Drama", "Sci-Fi"],
     "desc": "An alien stranded on Earth exposes hypocrisy in organized religion and society."},

    {"title": "Dilwale Dulhania Le Jayenge","language": "Hindi", "year": 1995, "rating": 8.1,
     "genres": ["Drama", "Romance"],
     "desc": "A young NRI follows the woman he loves across Europe to win her father's blessing."},

    {"title": "Lagaan",                    "language": "Hindi", "year": 2001, "rating": 8.1,
     "genres": ["Drama", "History", "Sport"],
     "desc": "Villagers stake their future on a cricket match against their British colonizers."},

    {"title": "Sholay",                    "language": "Hindi", "year": 1975, "rating": 8.2,
     "genres": ["Action", "Adventure", "Drama"],
     "desc": "Two outlaws are hired to capture the ruthless dacoit Gabbar Singh."},

    {"title": "Bajrangi Bhaijaan",         "language": "Hindi", "year": 2015, "rating": 8.1,
     "genres": ["Adventure", "Drama"],
     "desc": "A devotee of Hanuman helps a lost mute Pakistani girl find her way home."},

    {"title": "Queen",                     "language": "Hindi", "year": 2014, "rating": 8.1,
     "genres": ["Comedy", "Drama"],
     "desc": "A jilted bride travels solo on her honeymoon and rediscovers herself."},

    {"title": "Andhadhun",                 "language": "Hindi", "year": 2018, "rating": 8.3,
     "genres": ["Crime", "Music", "Mystery", "Thriller"],
     "desc": "A blind pianist stumbles into a murder and a deadly cat-and-mouse game of deception."},

    {"title": "Gangs of Wasseypur",        "language": "Hindi", "year": 2012, "rating": 8.3,
     "genres": ["Action", "Crime", "Drama"],
     "desc": "A generations-long coal-mafia revenge saga set in the heartland of Dhanbad."},

    {"title": "Taare Zameen Par",          "language": "Hindi", "year": 2007, "rating": 8.4,
     "genres": ["Drama"],
     "desc": "A compassionate art teacher recognises and nurtures a dyslexic child's hidden talents."},

    {"title": "Dil Chahta Hai",            "language": "Hindi", "year": 2001, "rating": 8.1,
     "genres": ["Comedy", "Drama", "Romance"],
     "desc": "Three best friends navigate love, ambition, and life after college."},

    {"title": "Mughal-E-Azam",             "language": "Hindi", "year": 1960, "rating": 8.2,
     "genres": ["Drama", "History", "Romance"],
     "desc": "Prince Salim defies the Mughal emperor for his forbidden love for dancer Anarkali."},

    {"title": "Article 15",               "language": "Hindi", "year": 2019, "rating": 8.1,
     "genres": ["Crime", "Drama", "Thriller"],
     "desc": "An IPS officer confronts deep-rooted caste discrimination while solving a brutal murder."},

    {"title": "Tumbbad",                   "language": "Hindi", "year": 2018, "rating": 8.2,
     "genres": ["Horror", "Mystery", "Thriller"],
     "desc": "A man's obsessive quest for a mythological treasure leads him into a cursed ancestral womb."},

    # ═══════════════════════════════════════════════════════════════════════════
    # KANNADA (SANDALWOOD) MOVIES (15)
    # ═══════════════════════════════════════════════════════════════════════════
    {"title": "KGF Chapter 1",             "language": "Kannada", "year": 2018, "rating": 8.2,
     "genres": ["Action", "Crime", "Drama"],
     "desc": "Rocky rises from the slums to seize control of the deadly Kolar Gold Fields."},

    {"title": "KGF Chapter 2",             "language": "Kannada", "year": 2022, "rating": 8.4,
     "genres": ["Action", "Crime", "Drama"],
     "desc": "Rocky's empire faces its greatest challenge as government forces and rivals close in."},

    {"title": "Ulidavaru Kandanthe",       "language": "Kannada", "year": 2014, "rating": 8.5,
     "genres": ["Crime", "Drama", "Thriller"],
     "desc": "One coastal crime, five perspectives — each revealing a different layer of truth."},

    {"title": "Kirik Party",               "language": "Kannada", "year": 2016, "rating": 8.2,
     "genres": ["Comedy", "Drama", "Music", "Romance"],
     "desc": "A rowdy engineering student transforms through friendship and a strong-willed girl's influence."},

    {"title": "777 Charlie",               "language": "Kannada", "year": 2022, "rating": 8.7,
     "genres": ["Adventure", "Drama"],
     "desc": "A lonely, closed-off man's life is forever changed by a stray dog named Charlie."},

    {"title": "Mungaru Male",              "language": "Kannada", "year": 2006, "rating": 8.0,
     "genres": ["Drama", "Romance"],
     "desc": "A young man falls for a woman already promised to another, amid monsoon rains and longing."},

    {"title": "Garuda Gamana Vrishabha Vahana","language": "Kannada", "year": 2021, "rating": 8.5,
     "genres": ["Action", "Crime", "Drama"],
     "desc": "Two childhood friends drift to opposite sides of the Mangalore criminal underworld."},

    {"title": "Thithi",                    "language": "Kannada", "year": 2015, "rating": 8.3,
     "genres": ["Comedy", "Drama"],
     "desc": "Three generations of a village family gather for a death anniversary with absurd results."},

    {"title": "Rangitaranga",              "language": "Kannada", "year": 2015, "rating": 8.2,
     "genres": ["Horror", "Mystery", "Thriller"],
     "desc": "A couple's documentary trip to a remote village turns into a supernatural nightmare."},

    {"title": "Godhi Banna Sadharana Mykattu","language": "Kannada", "year": 2016, "rating": 8.6,
     "genres": ["Drama"],
     "desc": "A son frantically searches Bangalore for his father, who has gone missing with Alzheimer's."},

    {"title": "Sangolli Rayanna",          "language": "Kannada", "year": 2012, "rating": 7.8,
     "genres": ["Action", "Biography", "History"],
     "desc": "The legendary freedom fighter of Kittur wages a fierce rebellion against the British."},

    {"title": "Avane Srimannarayana",      "language": "Kannada", "year": 2019, "rating": 7.6,
     "genres": ["Action", "Comedy", "Mystery"],
     "desc": "A lazy village constable accidentally stumbles upon a legendary hidden treasure."},

    {"title": "Pailwaan",                  "language": "Kannada", "year": 2019, "rating": 7.6,
     "genres": ["Action", "Drama", "Sport"],
     "desc": "A wrestler raised by a kind-hearted mentor battles corruption to reclaim his title."},

    {"title": "Lucia",                     "language": "Kannada", "year": 2013, "rating": 8.3,
     "genres": ["Mystery", "Sci-Fi", "Thriller"],
     "desc": "A theatre usher's dreams blur with reality after he starts taking a mysterious pill."},

    {"title": "Dia",                       "language": "Kannada", "year": 2020, "rating": 8.1,
     "genres": ["Drama", "Romance", "Thriller"],
     "desc": "A love triangle between childhood friends spirals into dark and devastating consequences."},
]

# ── Derive the master list of all unique genres (sorted) ─────────────────────
ALL_GENRES = sorted(set(g for m in MOVIES for g in m["genres"]))
ALL_LANGUAGES = sorted(set(m["language"] for m in MOVIES))
