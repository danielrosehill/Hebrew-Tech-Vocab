# Hebrew Tech Vocab List 

## Project 

For those who don't know me, I'm an Irish-born immigrant who moved to Israel ..... *squirms in embarrassment at state of Hebrew* .... a while. 

I thought I would create a repo to gather some translations for niche tech words. This is an updated take on an old Anki board project that I created in that dinosaur era that we lived through before the advent of AI.

The "reasoning": Google Translate (etc) are great but, from long experience, there's often a gulf between what they provide and ... what people actually say.

Also: 

Hebrew, like all languages, is in a constant state of flux. Tech vocab, in any language, is often new - and tends to propagate from English to international equivalents. 

Sometimes, there's both a more official word (often English or a direct transliteration like בלוטוס) and a word that is a more "correct" version that falls out of favor. 

## Method

The method here will be as follows:

- "Words wanted": I will populate a list of words that I want to get translations for. Claude/AI will identify gaps and bulk up my list. I will provide a word and an example sentence for disambiguation and clarity. 
- Pass 1: Machine/AI translation: Claude (etc) will provide its machine translation and source and sample sentence. To be thorough, I will also use Claude to classify whether there's a translation for it or if it's a transliteration or a word for which a true Hebrew equivalent has been found.  Claude will create one document per word in the machine translations folder which in turn will be organised into thematic subfolders. The documents will provide the word, the source, a sample usage, and any notes. 
- Pass 2: I will periodically attempt to bribe native Hebrew speakers with beer or appeal to their charitable instincts to review/contribute words. As often one word will have a few variations, I will capture this in JSON. If pass 2 is passed, it will have a boolean flag. 

dictionary.json will be the final source of truth.

In "flow 1": 

- Daniel defines words 
- Claude retrieves 
- Claude populates `machine-translations` and then `dictionary.json`. For human verified, the Boolean value is false.

In "flow 2"

- A human reviews the current dictionary 
- If they confirm, the entry gets a positive Boolean. If the human has any personal experience to convey like ("this isn't used much anymore") those are appended as human notes and a document is created in human notes.

## Learning Resources 

To facilitate spaced repetition, periodically, the dictionary is taken as the basis for creating a TTS generated "episode" for vocab learning and recap.

Process requires: English TTS, Hebrew TTS or multilingual TTS.
