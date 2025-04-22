
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 100,
  duration: '20s'
};

export default function () {
  const res = http.get('http://localhost:3001/room');
  check(res, {
    'status was 200': (r) => r.status === 200,
    'response contains rooms': (r) => r.json().rooms !== undefined,
  });
  sleep(1);
}
