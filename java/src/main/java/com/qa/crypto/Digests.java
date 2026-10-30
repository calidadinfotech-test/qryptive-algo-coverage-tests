package com.qa.crypto;

import java.security.MessageDigest;
import org.bouncycastle.crypto.Digest;
import org.bouncycastle.crypto.Xof;
import org.bouncycastle.crypto.digests.DSTU7564Digest;
import org.bouncycastle.crypto.digests.ParallelHash;
import org.bouncycastle.crypto.digests.SkeinDigest;
import org.bouncycastle.crypto.digests.TigerDigest;

public class Digests {

    public Digest ukrainianHash() {
        return new DSTU7564Digest(256);
    }

    public Digest wideBlockHash() {
        return new SkeinDigest(512, 512);
    }

    public Digest legacyTree() {
        return new TigerDigest();
    }

    public MessageDigest rivestSixHash() throws Exception {
        return MessageDigest.getInstance("MD6-256");
    }

    public MessageDigest sha3Finalist() throws Exception {
        return MessageDigest.getInstance("JH-256");
    }

    public MessageDigest koreanLegacyHash() throws Exception {
        return MessageDigest.getInstance("HAS-160");
    }

    public Xof parallelXof() {
        return new ParallelHash(128, null, 32);
    }
}
