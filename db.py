from app import app, Project, Community, db

projects = [
    {'name': 'INSTAGRAM AUTOMATION', 'img': '/static/img/sel.png', 'desc': 'Created a script to automate Instagram tasks, such as logging in, following users, liking posts, and downloading content.'},
    {'name': 'M&V FRONTEND', 'img': '/static/img/i2.png', 'desc': """I created a project for a fictional clothing brand that specializes in selling medical
                                scrubs. The project utilizes a variety of CSS techniques to create an elegant and
                                interactive user interface."""},
    {'name': 'UNI-TIMETABLE ORGANIZER', 'img': '/static/img/I3.png', 'desc': """Utilized Pandas to streamline the process of retrieving university class
                                schedules. Created a user-friendly system where students can input their course
                                code to quickly access the timing and location of their classes, significantly
                                speeding up the process compared to traditional methods."""},
]

communities = [
    {'name': 'GDG Nicosia', 'img': '/static/img/gdg.png', 'role': 'Board Admin'},
    {'name': 'CodeCrafters', 'img': '/static/img/cc.jpeg', 'role': 'Coding Ambassador'},
    {'name': 'NEU Biomedical', 'img': '/static/img/bme.jpeg', 'role': 'Member'},
    {'name': 'NEU', 'img': 'none', 'role': 'member'},
]

with app.app_context():
    
    db.create_all()

    for project_data in projects:
        project = Project(**project_data)
        db.session.add(project)

    for community_data in communities:
        community = Community(**community_data)
        db.session.add(community)

    db.session.commit()

    print("Projects added to the database.")
