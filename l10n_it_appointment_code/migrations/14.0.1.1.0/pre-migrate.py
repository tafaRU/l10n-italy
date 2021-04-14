# Copyright 2021 Alex Comba - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.update_module_names(
        env.cr,
        [
            ("l10n_it_codice_carica", "l10n_it_appointment_code"),
        ],
    )
    openupgrade.rename_models(
        env.cr,
        [
            ("codice.carica", "appointment.code"),
        ],
    )
    openupgrade.rename_tables(
        env.cr,
        [
            ("codice_carica", "appointment_code"),
        ],
    )
    openupgrade.rename_xmlids(
        env.cr,
        [
            (
                "l10n_it_codice_carica.view_codice_carica_tree",
                "l10n_it_appointment_code.view_appointment_code_tree",
            ),
            (
                "l10n_it_codice_carica.view_codice_carica_form",
                "l10n_it_appointment_code.view_appointment_code_form",
            ),
            (
                "l10n_it_codice_carica.action_codice_carica",
                "l10n_it_appointment_code.action_appointment_code",
            ),
            (
                "l10n_it_codice_carica.menu_codice_carica",
                "l10n_it_appointment_code.menu_appointment_code",
            ),
        ],
    )
