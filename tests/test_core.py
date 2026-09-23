from teacher_ai_assessment.core import route_for_review, assessment_metrics
from teacher_ai_assessment.synthetic import make_assessments

def test_routing():
    assert route_for_review(4,1,.1)
    assert route_for_review(3,3,.4)
    assert not route_for_review(3,3,.1)

def test_metrics_bounds():
    m=assessment_metrics(make_assessments(200,2))
    assert 0<=m['review_rate']<=1
    assert -1<=m['quadratic_kappa']<=1
