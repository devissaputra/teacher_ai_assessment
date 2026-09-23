from __future__ import annotations
import pandas as pd
from sklearn.metrics import cohen_kappa_score

def route_for_review(human_score:int, ai_score:int, ai_uncertainty:float, max_gap:int=1, uncertainty_threshold:float=.28)->bool:
    return abs(human_score-ai_score)>max_gap or ai_uncertainty>=uncertainty_threshold

def assessment_metrics(df:pd.DataFrame)->dict:
    exact=(df.human_score==df.ai_score)
    within=(df.human_score-df.ai_score).abs()<=1
    review=[route_for_review(r.human_score,r.ai_score,r.ai_uncertainty) for r in df.itertuples()]
    return {'exact_agreement':float(exact.mean()),'within_one_agreement':float(within.mean()),'quadratic_kappa':float(cohen_kappa_score(df.human_score,df.ai_score,weights='quadratic')),'review_rate':float(sum(review)/len(review))}

def audit_rows(df:pd.DataFrame)->pd.DataFrame:
    out=df.copy(); out['needs_review']=[route_for_review(r.human_score,r.ai_score,r.ai_uncertainty) for r in out.itertuples()]
    out['final_status']=out.needs_review.map({True:'human_review_required',False:'provisional_alignment'})
    return out
