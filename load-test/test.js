import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  http.get('http://localhost:30080/healthz'); // Replace with actual NodePort IP
  sleep(0.5);
}
