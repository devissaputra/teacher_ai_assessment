import numpy as np, pandas as pd

def make_assessments(n=500,seed=19):
    rng=np.random.default_rng(seed); true=rng.integers(0,5,n)
    human=np.clip(true+rng.choice([-1,0,1],n,p=[.12,.76,.12]),0,4)
    err=rng.choice([-2,-1,0,1,2],n,p=[.04,.14,.64,.14,.04]); ai=np.clip(true+err,0,4)
    unc=np.clip(.12+.16*np.abs(err)+rng.normal(0,.06,n),.01,.95)
    return pd.DataFrame({'sample_id':[f'S{i:04d}' for i in range(n)],'human_score':human,'ai_score':ai,'ai_uncertainty':unc})
