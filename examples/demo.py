from pathlib import Path
import json
from teacher_ai_assessment.synthetic import make_assessments
from teacher_ai_assessment.core import assessment_metrics,audit_rows
root=Path(__file__).resolve().parents[1]; (root/'results').mkdir(exist_ok=True)
df=make_assessments(); audit=audit_rows(df); metrics=assessment_metrics(df)
audit.to_csv(root/'results'/'synthetic_audit_log.csv',index=False); (root/'results'/'demo_metrics.json').write_text(json.dumps({k:round(v,3) for k,v in metrics.items()},indent=2)); print(json.dumps({k:round(v,3) for k,v in metrics.items()},indent=2))
