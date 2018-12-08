// supervised naive Bayes

data {
  // training data
  int<lower=1> K;               // num topics  ---  CMV statuses (2)
  int<lower=1> V;               // num words   ---  TCR's
  int<lower=0> M;               // num docs    ---  People
  int<lower=0> N;               // total word instances  ---   TCR instances?
  int<lower=1,upper=K> z[M];    // topic for doc m   ---  CMV status of each person
  int<lower=1,upper=V> w[N];    // word n    ---  TCR instances in whole data
  int<lower=1,upper=M> doc[N];  // doc ID for word n    ---  TCR instances in each person
  // hyperparameters
  vector<lower=0>[K] alpha;     // topic prior
  vector<lower=0>[V] beta;      // word prior
}
parameters {
  simplex[K] theta;   // topic prevalence
  simplex[V] phi[K];  // word dist for topic k
}
model {
  // priors
  theta ~ dirichlet(alpha);
  for (k in 1:K)  
    phi[k] ~ dirichlet(beta);
  // likelihood, including latent category
  for (m in 1:M)
    z[m] ~ categorical(theta);
  for (n in 1:N)
    w[n] ~ categorical(phi[z[doc[n]]]);
}