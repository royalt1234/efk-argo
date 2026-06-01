# EFK Stack Deployment on Kubernetes

## Add Helm Repositories

```bash
helm repo add elastic https://helm.elastic.co
helm repo add fluent https://fluent.github.io/helm-charts
helm repo update
```

---

## Pull Helm Charts

```bash
helm pull elastic/elasticsearch --untar
helm pull elastic/kibana --untar
helm pull fluent/fluent-bit --untar
```

---

## Create Namespace

```bash
kubectl create namespace logging
```

---

## Deploy Elasticsearch

```bash
cd elasticsearch

helm install elasticsearch . \
  -n logging \
  -f values-custom.yaml
```

---

## Deploy Kibana

```bash
cd ../kibana

helm install kibana . \
  -n logging
```

---

## Deploy Fluent Bit

```bash
cd ../fluent-bit

helm install fluent-bit . \
  -n logging
```