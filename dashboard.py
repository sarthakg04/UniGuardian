from config import WEIGHTINGS, MAX_SCORES


class Dashboard:

    @staticmethod
    def generate_dashboard(student, analysis_results, verification_results, holistic_results, refined_results):
        total_score = sum(analysis_results[key] * WEIGHTINGS.get(key, 0) for key in analysis_results)

        insights = []

        if analysis_results['academic'] < 70:
            insights.append(
                "Academic performance (based on GPA) below average. Consider additional academic evaluations.")
        if analysis_results['essay'] < 10:
            insights.append(
                "Essay lacks strong sentiment or is too subjective. Consider a more in-depth essay analysis.")
        if verification_results['ai_generated_essay']:
            insights.append("Essay might be AI-generated. Needs further verification.")
        if holistic_results['background_adjustment'] > 1.0:
            insights.append("First-generation student. Might need additional support or resources.")

        dashboard_data = {
            'Student ID': student.get_id(),
            'Total Score': total_score,
            'Individual Scores': analysis_results,
            'Maximum Possible Scores': MAX_SCORES,
            'Standardized Tests': student.standardized_scores,
            'Verifications': verification_results,
            'Holistic Factors': holistic_results,
            'Refined Analysis': refined_results,
            'Insights': insights
        }

        return dashboard_data
