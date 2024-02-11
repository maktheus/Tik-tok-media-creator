from deepgram_captions import DeepgramConverter, webvtt

transcription = DeepgramConverter("/home/msuchoa/sideProjects/tikTokMediaCreator/src/Audio/_tmp_gradio_852bad66ec35249b9602a73c7f1cd840d577c9ab_output.wav")
captions = webvtt(transcription)