from textblob import TextBlob
from config import GPA_SCALE, MAX_SCORES


class Analysis:

    @staticmethod
    def academic_analysis(gpa, scale=None):
        # Use the provided scale or default to the config's GPA scale
        scale = scale or GPA_SCALE
        # Convert GPA to percentage
        return (gpa / scale) * 100

    @staticmethod
    def extracurricular_analysis(activities):
        weightages = {
            'debate_club': 10,
            'sports': 8,
            'volunteer_work': 7
        }
        score = sum(weightages.get(activity, 0) for activity in activities.keys())
        # Normalize to 100
        max_possible_score = sum(weightages.values())
        return (score / max_possible_score) * 100

    @staticmethod
    def essay_analysis(essay):
        analysis = TextBlob(essay)
        return ((analysis.sentiment.polarity + (1 - analysis.sentiment.subjectivity)) / 2) * 100

    @staticmethod
    def recommendation_analysis(recommendations):
        positive_keywords = ['excellent', 'brilliant', 'good', 'outstanding', 'leadership']
        score = sum(sum(1 for keyword in positive_keywords if keyword in rec.lower()) for rec in recommendations)
        max_score = len(recommendations) * len(positive_keywords)
        return (score / max_score) * 100

    @staticmethod
    def research_paper_verification(papers):
        reputed_journals = ['AI Journal', 'Nature', 'Computer Science Review']
        verified_papers = [paper for paper in papers if paper['journal'] in reputed_journals]
        return (len(verified_papers) / len(papers)) * 100

    @staticmethod
    def certification_verification(certifications):
        known_authorities = ['Coursera', 'Udacity', 'edX', 'CompTIA']
        verified_certs = [cert for cert in certifications if cert['authority'] in known_authorities]
        return (len(verified_certs) / len(certifications)) * 100

    @staticmethod
    def ai_generated_content_detection(essay):
        personal_pronouns = ['i', 'me', 'my', 'mine', 'we', 'us', 'our']
        if not any(pronoun in essay.lower() for pronoun in personal_pronouns):
            return True
        return False

    @staticmethod
    def background_adjustment(background_info):
        return 1.05 if background_info.get('first_generation') else 1.0

    @staticmethod
    def score_normalization(standardized_scores):
        weightings = {
            'SAT': 1.5,
            'TOEFL': 0.667
        }
        normalized_score = sum(standardized_scores[test] * weightings.get(test, 1) for test in standardized_scores)
        return normalized_score

    @staticmethod
    def achievements_analysis(extracurriculars):
        achievements_scores = {
            'debate_club': 10,
            'sports': 20,
            'volunteer_work': 15
        }
        score = sum(
            (1 if isinstance(extracurriculars[activity], bool) else 0.5) * achievements_scores.get(activity, 0) for
            activity in extracurriculars if extracurriculars[activity])
        # Normalize to 100
        max_possible_score = sum(achievements_scores.values())
        return (score / max_possible_score) * 100
