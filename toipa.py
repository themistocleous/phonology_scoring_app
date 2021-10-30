'''
Functions for phonetic transcription 
Charalambos Themistocleous 2019
'''
import subprocess


def phonetic(toipa):
    """This function provides the IPA transcription for unknown words."""
    p = subprocess.run(["espeak", "-q", "--ipa", "-v", "en-us"],
                       capture_output=True, text=True, input=toipa)
    output = p.stdout
    output = str(output)
    return output
