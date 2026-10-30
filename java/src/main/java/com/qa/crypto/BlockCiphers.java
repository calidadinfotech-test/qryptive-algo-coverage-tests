package com.qa.crypto;

import javax.crypto.Cipher;
import javax.crypto.Mac;
import org.bouncycastle.crypto.BlockCipher;
import org.bouncycastle.crypto.engines.AESEngine;
import org.bouncycastle.crypto.engines.DSTU7624Engine;
import org.bouncycastle.crypto.engines.GOST28147Engine;
import org.bouncycastle.crypto.engines.RC532Engine;
import org.bouncycastle.crypto.engines.RC6Engine;
import org.bouncycastle.crypto.engines.SkipjackEngine;
import org.bouncycastle.crypto.engines.TEAEngine;
import org.bouncycastle.crypto.engines.ThreefishEngine;
import org.bouncycastle.crypto.macs.CBCBlockCipherMac;
import org.bouncycastle.crypto.macs.VMAC;

public class BlockCiphers {

    public Cipher legacyEuropean() throws Exception {
        return Cipher.getInstance("IDEA/CBC/PKCS5Padding", "BC");
    }

    public Cipher koreanStandard() throws Exception {
        return Cipher.getInstance("SEED/CBC/PKCS5Padding", "BC");
    }

    public Cipher koreanGcm() throws Exception {
        return Cipher.getInstance("ARIA/GCM/NoPadding", "BC");
    }

    public Cipher koreanLightweight() throws Exception {
        return Cipher.getInstance("LEA/CTR/NoPadding");
    }

    public BlockCipher ukrainianStandard() {
        return new DSTU7624Engine(256);
    }

    public BlockCipher sovietStandard() {
        return new GOST28147Engine();
    }

    public BlockCipher clipperChip() {
        return new SkipjackEngine();
    }

    public BlockCipher tinyCipher() {
        return new TEAEngine();
    }

    public BlockCipher rivestFive() {
        return new RC532Engine();
    }

    public BlockCipher rivestSix() {
        return new RC6Engine();
    }

    public BlockCipher tweakableWide() {
        return new ThreefishEngine(512);
    }

    public org.bouncycastle.crypto.Mac chainedMac() {
        return new CBCBlockCipherMac(new AESEngine());
    }

    public org.bouncycastle.crypto.Mac vectorMac() {
        return new VMAC(new AESEngine());
    }

    public Mac universalMac() throws Exception {
        return Mac.getInstance("UMAC128");
    }
}
