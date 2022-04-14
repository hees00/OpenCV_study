import cv2
import sys

# cv2 버전 확인
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')


def main():
    tracker_types = [ 'BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE' ]
    tracker_type = tracker_types[ 2 ]

    if int(minor_ver) < 3 :
        tracler = cv2.Tracker_create(tracker_type)
    else :
        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
        if tracker_type == 'MOSSE':
            tracker = cv2.TrackerMOSSE_create()

        # #video
        # video = cv2.VideoCapture("./photo/tracking_test2.mp4")
        #
        #
        # if not video.isOpened():
        #     print("Could not open video")
        #     sys.exit()

        # # Read first frame.
        # ok, frame = video.read()
        #
        # if not ok:
        #     print('Cannot read video file')
        #     sys.exit()
        #
        cap1 = cv2.VideoCapture(0)

        if (cap1.isOpened()):
            ok, frame = cap1.read()
        else:
            ret1 = False
            print("안열림")


        # frame = cv2.resize(frame, dsize=(500, 500), interpolation=cv2.INTER_AREA)

        # 미리 객체를 지정해줄 때
        # bbox = (x,y,x+w,y+h)

        # Uncomment the line below to select a different bounding box
        bbox = cv2.selectROI(frame, False)

        # Initialize tracker with first frame and bounding box
        ok = tracker.init(frame, bbox)

        while True:

            # ok, frame = video.read()
            # frane = cv2.resize(frame,dsize=(500,500),interpolation=cv2.INTER_AREA)
            # if not ok:
            #     break

            ok, frame = cap1.read()
            if not ok:
                break

            # Start timer
            timer = cv2.getTickCount()

            # Update tracker
            ok, bbox = tracker.update(frame)
            cv2.putText(frame, "(x,y,w,h) : " + str(bbox), (500, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[ 0 ]), int(bbox[ 1 ]))
                p2 = (int(bbox[ 0 ] + bbox[ 2 ]), int(bbox[ 1 ] + bbox[ 3 ]))
                cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
            else:
                # Tracking failure
                cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255),
                            2)

            # Display tracker type on frame
            cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

            # Display FPS on frame
            cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

            # Display result
            cv2.imshow("Tracking", frame)
            # key = cv2.waitKey(1)
            if cv2.waitKey(1) == 27 :
                break
            # if key == ord(' ') or (video_src != 0 and isFirst):
            #     ifFirst = False
            #     roi = cv2.selectROI("selectroi",frame,False)
            #     if roi[2] and roi[3]:
            #         tracker = trackers[trackerIdx]
            #         isInit = tracker.init(frame,roi)





if __name__ == '__main__':
    main()
