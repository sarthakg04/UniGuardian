import cryptocode

message = "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"
encoded = cryptocode.encrypt("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","openaiapi")
print(encoded)
decoded = cryptocode.decrypt(encoded, "openaiapi")
print(decoded)