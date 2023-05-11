from speechbrain.pretrained import EncoderASR

model = EncoderASR.from_hparams("my", savedir="my")

result = model.transcribe_file("file.wav")
# print(model)
print(result)

