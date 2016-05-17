package oracle;

public class SomeClassNew {


    public String getNomCache(String codeApp, String nom, String valeur,
                              String codeLangue) {

        return addCodeApplication(codeApp) + nom + addValeur(valeur) +
            addCodeLangue(codeLangue);

    }

    private String addCodeApplication(String codeApp) {
        if ((codeApp != null) && (getCodeApplication() != null) &&
            !codeApp.equals(getCodeApplication())) {
            return codeApp + ".";
        }
    }

    private String addCodeLangue(String codeLangue) {
        if (codeLangue != null)
            return codeLangue;
    }

    private String addValeur(String valeur) {
        if (valeur != null)
            return "." + valeur;
    }

    /** méthode requise pour le bien de l'exemple */
    private String getCodeApplication() {
        // return GestionSecurite.getInstance().getCodeApplication();
        return "codeApp";
    }

}

