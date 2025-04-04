
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,           // Number of virtual users
  duration: '30s',   // Test duration
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests should complete within 500ms
  },
};

export default function() {
  // Make HTTP request to the metrics endpoint
  const response = http.get('http://localhost:5000/metrics');
  
  // Check if request was successful
  check(response, {
    'status is 200': (r) => r.status === 200,
  });
  
  // Parse the response body as JSON
  const metrics = JSON.parse(response.body);
  
  // Log metrics for each virtual user (VU)
  console.log(`VU: ${__VU}, Iteration: ${__ITER}, CPU Usage: ${metrics.cpu_usage}, Memory Usage: ${metrics.memory_usage}`);
  
  // Add tags to the metrics for better visualization in k6 results
  response.tags['cpu_usage'] = metrics.cpu_usage;
  response.tags['memory_usage'] = metrics.memory_usage;
  
  // Optional: Add a sleep time between requests to simulate realistic user behavior
  sleep(1);
}
