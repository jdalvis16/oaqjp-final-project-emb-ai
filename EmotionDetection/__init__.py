"""EmotionDetection package.

Exposes the :func:`emotion_detector` function at the package level so it
can be imported as ``from EmotionDetection import emotion_detector``.
"""
# pylint: disable=invalid-name
# (the package name is fixed by the project spec as "EmotionDetection")

from EmotionDetection.emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
