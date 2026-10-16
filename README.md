# 🎧 Headbrr PLUS

**The upgraded headphone tester. Fully offline, safer, and a lot more capable than Headbrr.**

Flask + Web Audio. No CDN, no internet needed after install.

## What's new vs. Headbrr

| | Headbrr | **Headbrr PLUS** |
|---|---|---|
| Works offline | No (CDN: Tailwind, fonts, icons) | **Yes, zero external requests** |
| Meters | Fake mono average | **Real L/R RMS + peak hold + clip LEDs, in dB** |
| Visuals | none | **Log spectrum + dual-channel oscilloscope** |
| Waveforms | Sine | **Sine, Square, Triangle, Saw** |
| Frequency control | Linear slider | **Log slider, number input, 1/3-octave steps, note + cents** |
| Channel select | Separate test only | **Left / Both / Right on any signal** |
| Sweep | 10s up | **5/10/20/40s, up or down, loop** |
| Noise | White, Pink | **White, Pink, Brown** (seamless loop) |
| Stereo tests | Left / Right | **Ping, Ping-pong, L-R pan sweep** |
| Bass | none | **Bass steps 20-100 Hz (rattle check)** |
| Safety | none | **Limiter, dB volume, loud warning, click-free fades** |
| Hotkeys | none | **Space, Esc, arrows, L/B/R, S** |

## Install

```bash
git clone https://github.com/chambtai-sys/Headbrr-PLUS.git
cd Headbrr-PLUS
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. Options: `--host`, `--port`.
(PLUS binds to localhost by default; use `--host 0.0.0.0` to expose it on your network.)

## Hotkeys

`Space` start/stop · `Esc` stop all · `←/→` -/+ 1/3 octave · `↑/↓` volume · `L` `B` `R` channel · `S` sweep

## Safety

Output goes through a limiter, volume is in dB (default -24), and a warning shows above -12 dB. Start low with headphones on.

## License

MIT
