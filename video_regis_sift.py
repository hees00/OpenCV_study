##object 좌표 받기 해보는중

import numpy as np
import cv2

# path = "C:\\Users\\User\\Desktop\\ssu\\photo\\"
# imgpath1 = path + "lu.jpg"
# imgpath2 = path + "ru.jpg"

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')



def main():
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)

    if (cap1.isOpened() & cap2.isOpened()):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        cut = 1
    elif(cap1.isOpened()):
        ret2 = False
        ret1 = True
        print("cap2 안켜짐")
    elif(cap2.isOpened()):
        ret1 = False
        ret2 = True
        print("cap1 안켜짐")
    else:
        ret2 = False
        ret1 = False
        print("둘 다 안켜짐")

    tracker_types = [ 'BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE' ]
    tracker_type = tracker_types[ 2 ]

    if int(minor_ver) < 3:
        tracler = cv2.Tracker_create(tracker_type)
    else:
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



    while (ret1 and ret2):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        frame1 = cv2.resize(frame1, dsize=(500, 500), interpolation=cv2.INTER_AREA)
        frame2 = cv2.resize(frame2, dsize=(500, 500), interpolation=cv2.INTER_AREA)



        if cut == 1:
            gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

            sift = cv2.xfeatures2d.SIFT_create()

            kp1, des1 = sift.detectAndCompute(gray1, None)
            kp2, des2 = sift.detectAndCompute(gray2, None)

            bf = cv2.BFMatcher_create()
            matches = bf.match(des1, des2)
            sorted_matches = sorted(matches, key=lambda x: x.distance)
            res = cv2.drawMatches(frame1, kp1, frame2, kp2, sorted_matches[ :30 ], None, flags=2)
            cv2.imshow('match', res)

            src = np.float32([ kp1[ m.queryIdx ].pt for m in sorted_matches ]).reshape((-1, 1, 2))
            dst = np.float32([ kp2[ m.trainIdx ].pt for m in sorted_matches ]).reshape((-1, 1, 2))
            H, status = cv2.findHomography(dst, src, cv2.RANSAC, 5.0)
            print(H)


        output = cv2.warpPerspective(frame2, H, (frame1.shape[1] + frame2.shape[1], frame1.shape[0]))
        cv2.imshow("frame11",output)
        output[ 0: frame1.shape[ 0 ], 0: frame1.shape[ 1 ] ] = frame1

        if cut == 1:
            bbox = cv2.selectROI(output, False)
            bbox_2 = (bbox[0],bbox[1],1)
            H_back = np.linalg.inv(H)
            afterpos = bbox_2 @ H_back
            print("after homography" +str(afterpos))

            # Initialize tracker with first frame and bounding box)
            ok = tracker.init(output, bbox)
            ok = tracker.init(frame1, bbox)
            ok = tracker.init(frame2, bbox)
            cut = 0

        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(output)
        ok_cap1, bbox_cap1 = tracker.update(frame1)
        ok_cap2, bbox_cap2 = tracker.update(frame2)

        afterpos = bbox_2 @ H_back
        # print("after homography" + str(afterpos))
        cv2.putText(output, "(x,y,w,h) : " + str(bbox), (500, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);
        cv2.putText(frame1, "(x,y,w,h) : " + str(afterpos), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);
        cv2.putText(frame2, "(x,y,w,h) : " + str(bbox_cap2), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[ 0 ]), int(bbox[ 1 ]))
            p2 = (int(bbox[ 0 ] + bbox[ 2 ]), int(bbox[ 1 ] + bbox[ 3 ]))
            p1_cap1 = (int(bbox_cap1[ 0 ]), int(bbox_cap1[ 1 ]))
            p2_cap1 = (int(bbox_cap1[ 0 ] + bbox_cap1[ 2 ]), int(bbox_cap1[ 1 ] + bbox_cap1[ 3 ]))
            p1_cap2 = (int(bbox_cap2[ 0 ]), int(bbox_cap2[ 1 ]))
            p2_cap2 = (int(bbox_cap2[ 0 ] + bbox_cap2[ 2 ]), int(bbox_cap2[ 1 ] + bbox_cap2[ 3 ]))
            cv2.rectangle(output, p1, p2, (255, 0, 0), 2, 1)
            cv2.rectangle(frame1, p1_cap1, p2_cap2, (255, 0, 0), 2, 1)
            cv2.rectangle(frame2, p1_cap2, p2_cap2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            cv2.putText(output, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255),2)
        if ok_cap1:
            # Tracking success
            p1_cap1 = (int(bbox_cap1[ 0 ]), int(bbox_cap1[ 1 ]))
            p2_cap1 = (int(bbox_cap1[ 0 ] + bbox_cap1[ 2 ]), int(bbox_cap1[ 1 ] + bbox_cap1[ 3 ]))
            cv2.rectangle(frame1, p1_cap1, p2_cap2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            cv2.putText(frame1, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255),2)

        if ok_cap2:
            p2_cap2 = (int(bbox_cap2[ 0 ] + bbox_cap2[ 2 ]), int(bbox_cap2[ 1 ] + bbox_cap2[ 3 ]))
            cv2.rectangle(frame2, p1_cap2, p2_cap2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            cv2.putText(frame2, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255),2)

        # Display tracker type on frame
        cv2.putText(output, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        # Display FPS on frame
        cv2.putText(output, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        # Display result
        cv2.imshow("video1", frame1)
        cv2.imshow("video2", frame2)
        cv2.imshow("Tracking", output)
        # cv2.imshow("output", output)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    cap1.release()
    cap2.release()


if __name__ == "__main__":
    main()


