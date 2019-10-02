### Debugging celery performance issue with SQS broker

#### Pre-requisite
- have docker installed

### Running tests

`./test.sh <version>`

available `version`:
- celery4.1.0_kombu4.1.0
- celery4.2.0_kombu4.2.1
- celery4.2.0_kombu4.3.0
- celery4.3.0_kombu4.6.5
- celery4.4.0_kombu4.6.5
 

### Results
- On a MacBook Pro (15-inch, 2018)
    - celery4.1.0_kombu4.1.0 `~3s`
    - celery4.2.0_kombu4.2.1 `~3s`
    - celery4.2.0_kombu4.3.0 `~10s`
    - celery4.3.0_kombu4.6.5 `~10s`
    - celery4.4.0_kombu4.6.5 (rc3) `~10s`
   
 ### Observations
 - when using kombu >= 4.3.0, messages(10?) seems to be read every 1 second regardless of the number of tasks in queue.
