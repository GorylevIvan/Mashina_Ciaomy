import time
import numpy as np


def make_timestamps(fps: int, st_ts: float, fn_ts: float) -> np.ndarray:
    """
    Create array of timestamps. This array is discretized with fps,
    but not evenly.
    Timestamps are assumed sorted nad unique.
    Parameters:
    - fps: int
        Average frame per second
    - st_ts: float
        First timestamp in the sequence
    - fn_ts: float
        Last timestamp in the sequence
    Returns:
        np.ndarray: synthetic timestamps
    """
    # generate uniform timestamps
    timestamps = np.linspace(st_ts, fn_ts, int((fn_ts - st_ts) * fps))
    # add an fps noise
    timestamps += np.random.randn(len(timestamps))
    timestamps = np.unique(np.sort(timestamps))
    return timestamps


def match_timestamps(timestamps1: np.ndarray, timestamps2: np.ndarray) -> np.ndarray:
    """
    Timestamp matching function. It returns such array `matching` of length len(timestamps1),
    that for each index i of timestamps1 the output element matching[i] contains
    the index j of timestamps2, so that the difference between
    timestamps2[j] and timestamps1[i] is minimal.
    """
    # МОЙ КОД
    """
    Я реализовал сие задачу через два указателя 
    Сложность этого чуда О(n+m), мне так сказали умные люди, а я склонен умным людям верить
    """
    matching = np.empty(len(timestamps1), dtype=int)
    j = 0
    for i in range(len(timestamps1)):

        while (j + 1 < len(timestamps2) and
            abs(timestamps2[j + 1] - timestamps1[i]) < abs(timestamps2[j] - timestamps1[i])):
            j += 1

        matching[i] = j
    return matching
    #КОНЕЦ МОЕГО КОДА


def main():
    """
    Setup:
        Say we have two cameras, each filming the same scene. We make
        a prediction based on this scene (e.g. detect a human pose).
        To improve the robustness of the detection algorithm,
        we average the predictions from both cameras at each moment.
        The camera data is a pair (frame, timestamp), where the timestamp
        represents the moment when the frame was captured by the camera.
    Problem:
        For each frame of camera1, we need to find the index of the
        corresponding frame received by camera2. The frame i from camera2
        corresponds to the frame j from camera1, if
        abs(timestamps[i] - timestamps[j]) is minimal for all i.
    """
    # generate timestamps for the first camera
    timestamps1 = make_timestamps(30, time.time(), time.time() + 3600)
    # generate timestamps for the second camera
    timestamps2 = make_timestamps(60, time.time(), time.time() + 3600)
    matching = match_timestamps(timestamps1, timestamps2)
    #print(matching)


if __name__ == '__main__':
    main()
