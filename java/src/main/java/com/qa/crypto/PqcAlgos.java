package com.qa.crypto;

import java.security.Signature;
import javax.crypto.KeyAgreement;

public class PqcAlgos {

    public KeyAgreement retiredLatticeKem() throws Exception {
        return KeyAgreement.getInstance("NewHope", "BCPQC");
    }

    public Signature statefulHashSigner() throws Exception {
        return Signature.getInstance("LMS", "BCPQC");
    }
}
