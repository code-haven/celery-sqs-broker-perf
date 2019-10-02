### Debugging celery performance issue with SQS broker

#### Pre-requisite
- have docker installed

### Running tests
`./test-celery_4.1.0.sh`

`./test-celery_4.3.0.sh`

### Results
- On a MacBook Pro (15-inch, 2018)
  * celery 4.1.0: `~3s`
  * celery 4.3.0: `~10s`
   
 ### Observations
 - In celery 4.3.0, messages(10?) seems to be read every 1 second regardless of the number of tasks in queue.
