
# Add repos

helm repo add elastic https://helm.elastic.co
helm repo add fluent https://fluent.github.io/helm-charts
helm repo update

# pull helm charts

helm pull elastic/elasticsearch --untar 
helm pull elastic/kibana --untar 
helm pull fluent/fluent-bit --untar

# Create namespace

kubectl create namespace logging

# Install

helm install elasticsearch -n logging -f values-custom.yaml .
helm install kibana . -n logging
helm install fluent-bit . -n logging

