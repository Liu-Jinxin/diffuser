import os
import numpy as np
import imageio

def _make_dir(filename):
    folder = os.path.dirname(filename)
    if not os.path.exists(folder):
        os.makedirs(folder)

def save_video(filename, video_frames, fps=60, video_format='mp4'):
    assert fps == int(fps), fps
    _make_dir(filename)

    # Ensure video_frames is uint8 and in RGB format
    video_frames = np.asarray(video_frames)
    if video_frames.dtype != np.uint8:
        video_frames = (255 * np.clip(video_frames, 0, 1)).astype(np.uint8)
    if video_frames.shape[-1] == 3:
        # If frames are BGR (from OpenCV), convert to RGB
        # Assume input is RGB, if not, user should convert before
        pass

    with imageio.get_writer(filename, fps=int(fps), format=video_format) as writer:
        for frame in video_frames:
            writer.append_data(frame)

def save_videos(filename, *video_frames, axis=1, **kwargs):
    ## video_frame : [ N x H x W x C ]
    video_frames = np.concatenate(video_frames, axis=axis)
    save_video(filename, video_frames, **kwargs)
